from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / 'data' / 'raw'
PROCESSED_DIR = PROJECT_ROOT / 'data' / 'processed'
MODELS_DIR = PROJECT_ROOT / 'models'

RAW_FILE = RAW_DIR / 'MICRODADOS_ENCCEJA_2024_REG_NAC.csv'
PROCESSED_FILE = PROCESSED_DIR / 'encceja_knn.csv'
MODEL_FILE = MODELS_DIR / 'knn_pipeline.joblib'
METRICS_FILE = MODELS_DIR / 'metrics.json'

FEATURES = [
    'TP_CERTIFICACAO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'SG_UF_PROVA',
    'Q40', 'Q42', 'Q44', 'Q48', 'Q50', 'Q52', 'Q53', 'Q56', 'Q68'
]

TARGETS = [
    'NU_NOTA_LC', 'NU_NOTA_CH', 'NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_REDACAO'
]

ORDINAL_FEATURES = ['TP_FAIXA_ETARIA', 'Q40', 'Q42', 'Q68']
CATEGORICAL_FEATURES = [c for c in FEATURES if c not in ORDINAL_FEATURES]

TARGET_LABELS = {
    'NU_NOTA_LC': 'Linguagens',
    'NU_NOTA_CH': 'Ciências Humanas',
    'NU_NOTA_MT': 'Matemática',
    'NU_NOTA_CN': 'Ciências da Natureza',
    'NU_NOTA_REDACAO': 'Redação',
}

QUESTION_LABELS = {
    'TP_CERTIFICACAO': 'Tipo de certificação',
    'TP_FAIXA_ETARIA': 'Faixa etária',
    'TP_SEXO': 'Sexo',
    'SG_UF_PROVA': 'UF da prova',
    'Q40': 'Escolaridade do pai',
    'Q42': 'Escolaridade da mãe',
    'Q44': 'Situação de trabalho',
    'Q48': 'Renda mensal individual',
    'Q50': 'Renda mensal familiar',
    'Q52': 'Zona onde mora',
    'Q53': 'Condição da moradia',
    'Q56': 'Dispositivo eletrônico mais usado',
    'Q68': 'Frequência semanal de leitura',
}

CERTIFICATION_LABELS = {1: 'Ensino Fundamental', 2: 'Ensino Médio'}
SEX_LABELS = {'M': 'Masculino', 'F': 'Feminino'}
WORK_LABELS = {
    'A': 'Trabalho remunerado',
    'B': 'Trabalho sem remuneração',
    'C': 'Não trabalha',
}
INCOME_LABELS = {
    'A': 'Nenhuma renda',
    'B': 'Até 1 salário mínimo',
    'C': 'De 1 a 2 salários mínimos',
    'D': 'De 2 a 3 salários mínimos',
    'E': 'De 3 a 4 salários mínimos',
    'F': 'De 4 a 5 salários mínimos',
    'G': 'Acima de 5 salários mínimos',
}
FAMILY_INCOME_LABELS = {**INCOME_LABELS, 'H': 'Não sei'}
ZONE_LABELS = {'A': 'Zona rural', 'B': 'Zona urbana'}
HOUSING_LABELS = {
    'A': 'Casa alugada', 'B': 'Casa cedida', 'C': 'Casa financiada',
    'D': 'Casa própria', 'E': 'Situação de rua', 'F': 'Unidade de acolhimento temporário'
}
DEVICE_LABELS = {'A': 'Aparelho celular', 'B': 'Computador', 'C': 'Tablet', 'D': 'Nenhum'}
READING_LABELS = {
    'A': 'Todos os dias', 'B': 'Três vezes ou mais por semana',
    'C': 'Menos de três vezes por semana', 'D': 'Nenhuma vez por semana'
}
AGE_LABELS = {
    1:'Menor de 17 anos', 2:'17 anos', 3:'18 anos', 4:'19 anos', 5:'20 anos',
    6:'21 anos', 7:'22 anos', 8:'23 anos', 9:'24 anos', 10:'25 anos',
    11:'26 a 30 anos', 12:'31 a 35 anos', 13:'36 a 40 anos', 14:'41 a 45 anos',
    15:'46 a 50 anos', 16:'51 a 55 anos', 17:'56 a 60 anos', 18:'61 a 65 anos',
    19:'66 a 70 anos', 20:'Mais de 70 anos'
}

# Questionário: ordem crescente representa escolaridade crescente.
PARENT_EDUCATION = {chr(64+i): i for i in range(1, 16)}

PARENT_EDUCATION_LABELS = {
    'A':'1ª série do ensino fundamental', 'B':'2ª série do ensino fundamental',
    'C':'3ª série do ensino fundamental', 'D':'4ª série do ensino fundamental',
    'E':'5ª série do ensino fundamental', 'F':'6ª série do ensino fundamental',
    'G':'7ª série do ensino fundamental', 'H':'8ª série do ensino fundamental',
    'I':'1ª série do ensino médio', 'J':'2ª série do ensino médio',
    'K':'3ª série do ensino médio', 'L':'Ensino superior',
    'M':'Pós-graduação', 'N':'Nunca estudou', 'O':'Não sei'
}

READING_FREQUENCY = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
AGE_NUMERIC = {i: i for i in range(1, 21)}
