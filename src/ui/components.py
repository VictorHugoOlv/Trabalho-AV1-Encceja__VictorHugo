import pandas as pd
import streamlit as st
from src.data.config import TARGET_LABELS


def show_prediction(prediction):
    cols = st.columns(5)
    for col, target in zip(cols, prediction):
        col.metric(TARGET_LABELS[target], f'{prediction[target]:.2f}')


def show_comparison(comparison):
    table = comparison.copy()
    table['previsao'] = table['previsao'].round(2)
    table['media_vizinhos'] = table['media_vizinhos'].round(2)
    table['diferenca'] = table['diferenca'].round(2)
    st.dataframe(table, use_container_width=True, hide_index=True)


def show_neighbors(neighbor_df):
    table = neighbor_df.copy()
    for target in TARGET_LABELS:
        if target in table:
            table[target] = table[target].round(2)
    st.dataframe(table, use_container_width=True, hide_index=True)
