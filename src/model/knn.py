import json
import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.data.config import (
    CATEGORICAL_FEATURES, FEATURES, MODEL_FILE, METRICS_FILE,
    ORDINAL_FEATURES, TARGETS
)
from src.data.preprocessing import prepare_features


def build_pipeline(n_neighbors=5):
    numeric = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler()),
    ])
    categorical = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore')),
    ])
    preprocessor = ColumnTransformer([
        ('numeric', numeric, ORDINAL_FEATURES),
        ('categorical', categorical, CATEGORICAL_FEATURES),
    ])
    return Pipeline([
        ('preprocessor', preprocessor),
        ('knn', KNeighborsRegressor(n_neighbors=n_neighbors, weights='distance', metric='euclidean', n_jobs=-1)),
    ])


def train_and_save(df, n_neighbors=5):
    X = prepare_features(df)
    y = df[TARGETS].astype(float)
    # Validação enxuta para não calcular uma matriz de distâncias gigantesca.
    # O modelo final abaixo é treinado com todos os registros elegíveis.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    if len(X_train) > 50000:
        X_train = X_train.sample(50000, random_state=42)
        y_train = y.loc[X_train.index]
    if len(X_test) > 1000:
        X_test = X_test.sample(1000, random_state=42)
        y_test = y.loc[X_test.index]

    validation_model = build_pipeline(n_neighbors)
    validation_model.fit(X_train, y_train)
    pred = validation_model.predict(X_test)

    metrics = {}
    for i, target in enumerate(TARGETS):
        mae = mean_absolute_error(y_test.iloc[:, i], pred[:, i])
        rmse = float(np.sqrt(mean_squared_error(y_test.iloc[:, i], pred[:, i])))
        metrics[target] = {'mae': float(mae), 'rmse': float(rmse)}

    final_model = build_pipeline(n_neighbors)
    final_model.fit(X, y)
    MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(final_model, MODEL_FILE)
    with open(METRICS_FILE, 'w', encoding='utf-8') as f:
        json.dump({'n_neighbors': n_neighbors, 'records': len(df), 'metrics': metrics}, f, ensure_ascii=False, indent=2)
    return final_model, metrics


def load_model():
    return joblib.load(MODEL_FILE)


def predict(model, candidate):
    X = prepare_features(pd.DataFrame([candidate]))
    values = model.predict(X)[0]
    return dict(zip(TARGETS, values))


def neighbors(model, candidate, training_targets, k=5):
    X = prepare_features(pd.DataFrame([candidate]))
    transformed = model.named_steps['preprocessor'].transform(X)
    estimator = model.named_steps['knn']
    distances, indices = estimator.kneighbors(transformed, n_neighbors=k)
    rows = training_targets.iloc[indices[0]].copy().reset_index(drop=True)
    rows['distancia'] = distances[0]
    rows['vizinho'] = np.arange(1, len(rows) + 1)
    return rows
