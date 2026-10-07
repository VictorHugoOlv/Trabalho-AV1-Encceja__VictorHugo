import pandas as pd
from src.data.config import TARGETS, TARGET_LABELS


def compare_prediction_with_neighbors(prediction, neighbor_df):
    rows = []
    for target in TARGETS:
        values = neighbor_df[target].astype(float)
        pred = float(prediction[target])
        mean = float(values.mean())
        rows.append({
            'disciplina': TARGET_LABELS[target],
            'previsao': pred,
            'media_vizinhos': mean,
            'diferenca': pred - mean,
            'posicao': 'acima' if pred > mean else ('abaixo' if pred < mean else 'igual')
        })
    return pd.DataFrame(rows)


def neighbor_approval_rate(neighbor_df):
    passed = []
    for _, row in neighbor_df.iterrows():
        objective = all(float(row[t]) >= 100 for t in TARGETS[:4])
        essay = float(row[TARGETS[4]]) >= 5
        passed.append(objective and essay)
    return sum(passed) / len(passed) if passed else 0.0
