# Metodologia da primeira versão

## Pergunta de decisão

Dado um candidato novo, quais notas são esperadas para um perfil semelhante ao observado nos microdados do ENCCEJA 2024 e qual nível de acompanhamento pedagógico pode ser recomendado?

## Variáveis

O conjunto inicial foi limitado às variáveis de perfil definidas na arquitetura do Projeto 1 — ENCCEJA. As notas não entram como atributos de entrada; elas são os alvos previstos.

## Tratamento

1. leitura do `REG_NAC`;
2. seleção das 13 características e 5 alvos;
3. conversão das notas para numérico;
4. remoção de registros sem alguma das cinco notas-alvo;
5. imputação das características faltantes dentro do pipeline;
6. transformação ordinal das variáveis de idade, escolaridade dos pais e leitura;
7. one-hot encoding das categóricas;
8. padronização das variáveis ordinais;
9. K-NN com `k=5` e pesos por distância.

## Saída gerencial

A saída não é apenas a previsão numérica. O sistema mostra:

- cinco notas estimadas;
- cinco vizinhos mais próximos;
- média dos vizinhos por área;
- diferença entre previsão e média dos vizinhos;
- percentual dos vizinhos que atende aos mínimos;
- risco estimado;
- áreas que precisam de reforço;
- recomendação textual.
