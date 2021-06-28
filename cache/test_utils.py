from datetime import date
from pytest import raises
from .utils import date_range


def test_date_range_with_valid_dates():
    assert tuple(date_range(date(2021, 6, 20), date(2021, 6, 23))) == (
        date(2021, 6, 20),
        date(2021, 6, 21),
        date(2021, 6, 22),
    )


def test_date_range_same_dates():
    assert tuple(date_range(date(2021, 6, 20), date(2021, 6, 20))) == ()


def test_invalid_dates():
    with raises(ValueError, match=r'older or equal'):
        next(date_range(date(2021, 6, 21), date(2021, 6, 20)))
