from src.analysis.recommendation import is_approved, risk_from_neighbors
from src.data.config import TARGETS


def test_approval_thresholds():
    good = {t: 100.0 for t in TARGETS[:4]}
    good[TARGETS[4]] = 5.0
    assert is_approved(good)


def test_risk_bands():
    assert risk_from_neighbors(0.2) == 'Alto'
    assert risk_from_neighbors(0.6) == 'Moderado'
    assert risk_from_neighbors(0.9) == 'Baixo'
