import pandas as pd
from src.data.preprocessing import clean_dataset, prepare_features
from src.data.config import FEATURES, TARGETS


def sample():
    row = {c: 'A' for c in FEATURES}
    row.update({t: 100.0 for t in TARGETS})
    row['TP_CERTIFICACAO'] = 2
    row['TP_FAIXA_ETARIA'] = 12
    return pd.DataFrame([row])


def test_clean_keeps_complete_target():
    df = clean_dataset(sample())
    assert len(df) == 1


def test_clean_removes_missing_target():
    df = sample()
    df.loc[0, 'NU_NOTA_MT'] = None
    assert len(clean_dataset(df)) == 0


def test_ordinal_encoding():
    x = prepare_features(sample())
    assert x.loc[0, 'Q40'] == 1
    assert x.loc[0, 'Q42'] == 1
    assert x.loc[0, 'Q68'] == 4
