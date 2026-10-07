import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data.config import PROCESSED_FILE
from src.data.loader import load_processed
from src.model.knn import train_and_save

if __name__ == '__main__':
    if not PROCESSED_FILE.exists():
        raise SystemExit('Execute primeiro: python scripts/prepare_data.py')
    df = load_processed()
    model, metrics = train_and_save(df, n_neighbors=5)
    print('Modelo treinado com sucesso.')
    for target, values in metrics.items():
        print(f'{target}: MAE={values["mae"]:.3f} | RMSE={values["rmse"]:.3f}')
