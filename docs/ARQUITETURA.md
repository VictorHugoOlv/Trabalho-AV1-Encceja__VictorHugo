# Arquitetura — 🎓 Projeto 1 — ENCCEJA

```text
                    ┌────────────────────────────┐
                    │ Microdados ENCCEJA 2024    │
                    │ REG_NAC.csv                │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │ src/data/loader.py         │
                    │ leitura da fonte           │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │ preprocessing.py           │
                    │ seleção / limpeza          │
                    │ imputação                  │
                    │ codificação / normalização │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │ src/model/knn.py           │
                    │ KNeighborsRegressor        │
                    │ k = 5                      │
                    └─────────────┬──────────────┘
                                  │
                 ┌────────────────┴────────────────┐
                 ▼                                 ▼
      ┌─────────────────────┐          ┌──────────────────────┐
      │ Previsão das notas  │          │ 5 vizinhos próximos  │
      └──────────┬──────────┘          └──────────┬───────────┘
                 │                                 │
                 └────────────────┬────────────────┘
                                  ▼
                    ┌────────────────────────────┐
                    │ comparison.py              │
                    │ comparação com vizinhos    │
                    └─────────────┬──────────────┘
                                  ▼
                    ┌────────────────────────────┐
                    │ recommendation.py          │
                    │ risco + recomendação       │
                    └─────────────┬──────────────┘
                                  ▼
                    ┌────────────────────────────┐
                    │ Streamlit — app.py         │
                    │ interface do gestor        │
                    └────────────────────────────┘
```

## Separação de responsabilidades

- `src/data`: acesso e preparação dos dados;
- `src/model`: treinamento, persistência, previsão e vizinhos;
- `src/analysis`: interpretação da saída do modelo;
- `src/ui`: apresentação de resultados;
- `app.py`: orquestração da interface;
- `scripts`: reprodução do pipeline de preparação e treinamento;
- `tests`: verificações automatizadas.
