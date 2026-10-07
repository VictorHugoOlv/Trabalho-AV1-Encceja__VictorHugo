import json
from pathlib import Path
import streamlit as st
import pandas as pd

from src.data.config import (
    AGE_LABELS, CERTIFICATION_LABELS, DEVICE_LABELS, FAMILY_INCOME_LABELS,
    HOUSING_LABELS, INCOME_LABELS, MODEL_FILE, PROCESSED_FILE, QUESTION_LABELS,
    READING_LABELS, SEX_LABELS, TARGETS, TARGET_LABELS, WORK_LABELS, ZONE_LABELS, PARENT_EDUCATION_LABELS
)
from src.data.loader import load_processed
from src.model.knn import load_model, neighbors, predict
from src.analysis.comparison import compare_prediction_with_neighbors
from src.analysis.recommendation import recommendation
from src.ui.components import show_comparison, show_neighbors, show_prediction

st.set_page_config(page_title='ENCCEJA — Apoio à Decisão', page_icon='🎓', layout='wide')

@st.cache_resource
def get_model():
    return load_model()

@st.cache_data
def get_training_targets():
    df = load_processed()
    return df[TARGETS]


def select_with_labels(label, options, labels):
    values = list(options)
    choice = st.selectbox(label, values, format_func=lambda x: labels.get(x, str(x)))
    return choice

st.title('🎓 ENCCEJA — Sistema de Apoio à Decisão Educacional')
st.caption('Trabalho AV1 — K-Nearest Neighbors (K-NN) | ENCCEJA 2024')

if not MODEL_FILE.exists() or not PROCESSED_FILE.exists():
    st.error('Modelo ou base processada não encontrados. Execute: python scripts/train.py')
    st.stop()

with st.sidebar:
    st.header('Perfil do candidato')
    certification = select_with_labels('Certificação pretendida', [1, 2], CERTIFICATION_LABELS)
    age = select_with_labels('Faixa etária', list(AGE_LABELS), AGE_LABELS)
    sex = select_with_labels('Sexo', ['M', 'F'], SEX_LABELS)
    uf = st.selectbox('UF da prova', ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'])
    q40 = select_with_labels('Escolaridade do pai', list(PARENT_EDUCATION_LABELS), PARENT_EDUCATION_LABELS)
    q42 = select_with_labels('Escolaridade da mãe', list(PARENT_EDUCATION_LABELS), PARENT_EDUCATION_LABELS)
    q44 = select_with_labels('Situação de trabalho', list(WORK_LABELS), WORK_LABELS)
    q48 = select_with_labels('Renda mensal individual', list(INCOME_LABELS), INCOME_LABELS)
    q50 = select_with_labels('Renda mensal familiar', list(FAMILY_INCOME_LABELS), FAMILY_INCOME_LABELS)
    q52 = select_with_labels('Zona onde mora', list(ZONE_LABELS), ZONE_LABELS)
    q53 = select_with_labels('Condição da moradia', list(HOUSING_LABELS), HOUSING_LABELS)
    q56 = select_with_labels('Dispositivo eletrônico mais usado', list(DEVICE_LABELS), DEVICE_LABELS)
    q68 = select_with_labels('Frequência semanal de leitura', list(READING_LABELS), READING_LABELS)
    run = st.button('Analisar candidato', type='primary', use_container_width=True)

candidate = {
    'TP_CERTIFICACAO': certification, 'TP_FAIXA_ETARIA': age, 'TP_SEXO': sex,
    'SG_UF_PROVA': uf, 'Q40': q40, 'Q42': q42, 'Q44': q44, 'Q48': q48,
    'Q50': q50, 'Q52': q52, 'Q53': q53, 'Q56': q56, 'Q68': q68,
}

st.info('A previsão estima as cinco notas a partir de candidatos históricos com perfil semelhante. Ela é uma ferramenta de apoio à decisão, não uma garantia de resultado.')

if run:
    model = get_model()
    training_targets = get_training_targets()
    prediction = predict(model, candidate)
    neighbor_df = neighbors(model, candidate, training_targets, k=5)
    comparison = compare_prediction_with_neighbors(prediction, neighbor_df)
    result = recommendation(prediction, neighbor_df)

    st.subheader('📊 Notas previstas')
    show_prediction(prediction)

    c1, c2 = st.columns(2)
    with c1:
        st.metric('Risco estimado', result['risco'])
    with c2:
        st.metric('Vizinhos que atendem aos mínimos', f"{result['taxa_aprovacao_vizinhos'] * 100:.0f}%")

    st.subheader('🔎 Comparação com os vizinhos')
    show_comparison(comparison)

    st.subheader('👥 Cinco vizinhos mais próximos')
    display_neighbors = neighbor_df.rename(columns=TARGET_LABELS)[['vizinho','distancia'] + list(TARGET_LABELS.values())]
    show_neighbors(display_neighbors)

    st.subheader('💡 Recomendação ao gestor')
    if result['areas_abaixo_minimo']:
        st.warning(result['mensagem'])
    else:
        st.success(result['mensagem'])

    st.caption('Critério de referência usado na análise: 100 pontos em cada prova objetiva e 5,0 na redação, conforme o Leia-me dos microdados do ENCCEJA 2024.')
else:
    st.subheader('Como usar')
    st.markdown('1. Preencha o perfil na barra lateral.  \n2. Clique em **Analisar candidato**.  \n3. Observe as notas previstas, os cinco vizinhos, a comparação e a recomendação.')
