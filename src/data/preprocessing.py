import pandas as pd
from .config import FEATURES, TARGETS, ORDINAL_FEATURES, CATEGORICAL_FEATURES


def clean_dataset(df):
    data = df[FEATURES + TARGETS].copy()
    for col in TARGETS:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    # Para treinar previsão das cinco notas, o alvo precisa estar completo.
    data = data.dropna(subset=TARGETS).reset_index(drop=True)

    # Mantemos ausências nas características para que o pipeline faça imputação.
    # Isso evita transformar ausência de resposta em uma categoria artificial de baixo desempenho.
    return data


def transform_ordinal_features(df):
    data = df.copy()
    data['TP_FAIXA_ETARIA'] = pd.to_numeric(data['TP_FAIXA_ETARIA'], errors='coerce')
    data['Q40'] = data['Q40'].map(lambda x: ord(str(x).upper()) - 64 if pd.notna(x) else None)
    data['Q42'] = data['Q42'].map(lambda x: ord(str(x).upper()) - 64 if pd.notna(x) else None)
    data['Q68'] = data['Q68'].map({'A': 4, 'B': 3, 'C': 2, 'D': 1})
    return data


def prepare_features(df):
    data = transform_ordinal_features(df[FEATURES].copy())
    return data
