import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
from src.data.config import RAW_FILE, PROCESSED_FILE, FEATURES, TARGETS
from src.data.loader import load_raw_selected
from src.data.preprocessing import clean_dataset


def main():
    print(f'Carregando: {RAW_FILE}')
    df = load_raw_selected()
    print(f'Registros originais: {len(df):,}')
    clean = clean_dataset(df)
    print(f'Registros com as cinco notas disponíveis: {len(clean):,}')
    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    clean.to_csv(PROCESSED_FILE, index=False, encoding='utf-8')
    print(f'Gravado: {PROCESSED_FILE}')

if __name__ == '__main__':
    main()
