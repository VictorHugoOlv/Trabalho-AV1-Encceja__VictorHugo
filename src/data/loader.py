import pandas as pd
from .config import RAW_FILE, FEATURES, TARGETS


def load_raw_selected(path=RAW_FILE):
    cols = FEATURES + TARGETS
    return pd.read_csv(path, sep=';', encoding='latin1', usecols=cols, low_memory=False)


def load_processed(path=None):
    from .config import PROCESSED_FILE
    return pd.read_csv(path or PROCESSED_FILE)
