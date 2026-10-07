# Perfil dos dados utilizados

## Base principal

`MICRODADOS_ENCCEJA_2024_REG_NAC.csv`

- Registros originais: **834.648**
- Variáveis originais: **118**
- Registros com as cinco notas disponíveis: **161.004**

## Características do modelo

| Variável | Uso |
|---|---|
| TP_CERTIFICACAO | Tipo de certificação |
| TP_FAIXA_ETARIA | Faixa etária |
| TP_SEXO | Sexo |
| SG_UF_PROVA | UF |
| Q40 | Escolaridade do pai |
| Q42 | Escolaridade da mãe |
| Q44 | Situação de trabalho |
| Q48 | Renda individual |
| Q50 | Renda familiar |
| Q52 | Zona de residência |
| Q53 | Condição da moradia |
| Q56 | Dispositivo eletrônico mais usado |
| Q68 | Frequência semanal de leitura |

## Variáveis-alvo

| Campo | Nome apresentado |
|---|---|
| NU_NOTA_LC | Linguagens |
| NU_NOTA_CH | Ciências Humanas |
| NU_NOTA_MT | Matemática |
| NU_NOTA_CN | Ciências da Natureza |
| NU_NOTA_REDACAO | Redação |

## Outras bases percorridas

O pacote original também contém:

- `MICRODADOS_ENCCEJA_2024_PPL_NAC.csv`;
- `MICRODADOS_ENCCEJA_2024_PPL_NAC_QSE.csv`;
- `MICRODADOS_ENCCEJA_2024_ITENS_PROVA.csv`;
- dicionários XLSX/ODS;
- scripts SAS/SPSS;
- Leia-me dos microdados;
- matrizes de referência do Ensino Fundamental e Médio.

A primeira versão não mistura a população PPL com a base regular e não usa os itens de prova como características do K-NN. O dicionário e o Leia-me foram incorporados à pasta `docs` para rastreabilidade da preparação.
