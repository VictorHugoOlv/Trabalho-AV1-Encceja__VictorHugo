from src.data.config import TARGET_LABELS, TARGETS


def is_approved(prediction):
    return all(float(prediction[t]) >= 100 for t in TARGETS[:4]) and float(prediction[TARGETS[4]]) >= 5


def risk_from_neighbors(rate):
    if rate < 0.50:
        return 'Alto'
    if rate < 0.80:
        return 'Moderado'
    return 'Baixo'


def recommendation(prediction, neighbor_df):
    rate = 0.0
    if len(neighbor_df):
        approved = 0
        for _, row in neighbor_df.iterrows():
            if all(float(row[t]) >= 100 for t in TARGETS[:4]) and float(row[TARGETS[4]]) >= 5:
                approved += 1
        rate = approved / len(neighbor_df)
    risk = risk_from_neighbors(rate)

    deficits = []
    thresholds = {**{t: 100 for t in TARGETS[:4]}, TARGETS[4]: 5}
    for target in TARGETS:
        if float(prediction[target]) < thresholds[target]:
            deficits.append(TARGET_LABELS[target])

    if deficits:
        focus = ', '.join(deficits)
        action = f'Recomenda-se reforço e acompanhamento prioritário em: {focus}.'
    elif risk == 'Baixo':
        action = 'O perfil apresenta desempenho previsto acima dos critérios mínimos; recomenda-se acompanhamento regular.'
    else:
        action = 'Apesar da previsão atender aos mínimos, recomenda-se acompanhamento próximo devido ao histórico dos vizinhos.'

    return {
        'risco': risk,
        'taxa_aprovacao_vizinhos': rate,
        'areas_abaixo_minimo': deficits,
        'mensagem': action,
        'previsao_aprovacao': is_approved(prediction),
    }
