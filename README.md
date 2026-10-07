# 🎓 Trabalho AV1 — ENCCEJA

Sistema de Apoio à Tomada de Decisão Educacional usando **K-Nearest Neighbors (K-NN)**, desenvolvido para o trabalho da disciplina **Sistemas de Apoio à Tomada de Decisão**.

## 1. Objetivo

O sistema recebe o perfil socioeconômico/educacional de um novo candidato e utiliza candidatos históricos semelhantes do ENCCEJA 2024 para estimar:

- Linguagens;
- Ciências Humanas;
- Matemática;
- Ciências da Natureza;
- Redação.

A interface compara as previsões com os cinco vizinhos mais próximos, estima o percentual de vizinhos que atingiram os critérios mínimos e gera uma recomendação ao gestor do cursinho.

## 2. Arquitetura combinada — Projeto 1 — ENCCEJA

```text
ENCCEJA 2024 (REG_NAC)
        ↓
data/raw
        ↓
loader.py
        ↓
preprocessing.py
        ↓
Imputação + codificação + normalização
        ↓
KNeighborsRegressor
        ↓
5 vizinhos mais próximos
        ↓
Previsão das cinco notas
        ↓
comparison.py
        ↓
recommendation.py
        ↓
Streamlit (app.py)
```

A arquitetura é deliberadamente intermediária: **Python + Pandas/NumPy + Scikit-learn + Streamlit**, sem React, FastAPI ou banco de dados.

## 3. Estrutura

```text
Trabalho_AV1_ENCCEJA_v1/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   │   └── MICRODADOS_ENCCEJA_2024_REG_NAC.csv
│   └── processed/
│       └── encceja_knn.csv
├── models/
│   ├── knn_pipeline.joblib
│   └── metrics.json
├── src/
│   ├── data/
│   │   ├── config.py
│   │   ├── loader.py
│   │   └── preprocessing.py
│   ├── model/
│   │   └── knn.py
│   ├── analysis/
│   │   ├── comparison.py
│   │   └── recommendation.py
│   └── ui/
│       └── components.py
├── scripts/
│   ├── prepare_data.py
│   └── train.py
├── tests/
└── docs/
    ├── Dicionário_Microdados_ENCCEJA_2024.xlsx
    └── Leia-me_Microdados_ENCCEJA_2024.pdf
```

## 4. Base utilizada

A fonte principal é `MICRODADOS_ENCCEJA_2024_REG_NAC.csv`, do pacote oficial de microdados ENCCEJA 2024 fornecido para o trabalho.

A base original possui **834.648 participantes e 118 variáveis**. A primeira versão seleciona 13 características de perfil e usa as cinco notas como alvo.

### Características utilizadas

- `TP_CERTIFICACAO`
- `TP_FAIXA_ETARIA`
- `TP_SEXO`
- `SG_UF_PROVA`
- `Q40` — escolaridade do pai
- `Q42` — escolaridade da mãe
- `Q44` — situação de trabalho
- `Q48` — renda mensal individual
- `Q50` — renda mensal familiar
- `Q52` — zona onde mora
- `Q53` — condição da moradia
- `Q56` — dispositivo eletrônico mais usado
- `Q68` — frequência semanal de leitura

### Alvos

- `NU_NOTA_LC`
- `NU_NOTA_CH`
- `NU_NOTA_MT`
- `NU_NOTA_CN`
- `NU_NOTA_REDACAO`

## 5. Higienização

A base possui muitos participantes sem todas as cinco notas. Para o modelo de **previsão das cinco notas**, a primeira versão mantém somente registros que possuem as cinco notas disponíveis.

Resultado observado:

- Base original: **834.648** registros;
- Base elegível para treinamento: **161.004** registros.

As ausências das características de entrada não são transformadas em zero. O pipeline utiliza imputação pela mediana para variáveis ordinais e pela categoria mais frequente para variáveis categóricas.

## 6. Codificação e normalização

Variáveis ordinais:

- faixa etária;
- escolaridade do pai;
- escolaridade da mãe;
- frequência de leitura.

Essas variáveis são transformadas em valores numéricos e padronizadas com `StandardScaler`.

Variáveis categóricas são tratadas com `OneHotEncoder(handle_unknown='ignore')`.

## 7. K-NN

A primeira versão usa:

- `KNeighborsRegressor`;
- `k = 5`;
- distância Euclidiana;
- pesos por distância (`weights='distance'`).

O modelo prevê simultaneamente as cinco notas.

O arquivo `models/knn_pipeline.joblib` já contém o pipeline treinado com todos os 161.004 registros elegíveis.

## 8. Critério de referência para recomendação

O Leia-me dos microdados informa que o Inep sugere, para habilitação, **mínimo de 100 pontos em cada prova objetiva e 5,0 na redação**.

O sistema usa esse critério apenas para a camada de apoio à decisão:

```text
Linguagens >= 100
Humanas >= 100
Matemática >= 100
Natureza >= 100
Redação >= 5,0
```

A taxa de aprovação dos vizinhos é calculada sobre esses critérios.

Faixas de risco da primeira versão:

- menos de 50% dos vizinhos atendem aos mínimos → **Alto**;
- 50% a menos de 80% → **Moderado**;
- 80% ou mais → **Baixo**.

## 9. Executar

### Instalação

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

### Preparar novamente os dados

O CSV processado já está incluído. Para reconstruí-lo a partir da base original:

```bash
python scripts/prepare_data.py
```

### Treinar novamente

```bash
python scripts/train.py
```

### Executar interface

```bash
streamlit run app.py
```

## 10. Testes

```bash
pytest -q
```

## 11. Métricas da primeira versão

A validação foi feita com uma amostra de treinamento de até 50.000 registros e até 1.000 registros de teste para manter o cálculo de vizinhança viável localmente. O modelo final, usado pela interface, é treinado com todos os 161.004 registros elegíveis.

Consulte `models/metrics.json` para os valores de MAE e RMSE.

## 12. Observação acadêmica

Esta é uma **primeira versão completa e executável**. Ela foi estruturada para permitir evolução posterior sem misturar interface, tratamento de dados, modelo e regra de recomendação.
