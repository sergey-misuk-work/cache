from dataclasses import replace
from datetime import date
from django.core.cache import cache
from pytest import raises
from unittest.mock import call
from .cache import get_daily, get_total


def test_get_daily(response_external, daily_data, mocker):
    cache.clear()
    cache.set(str(date(2017, 6, 14)), daily_data[2])
    api_get = mocker.patch('cache.cache.get')
    api_get.side_effect = (
        replace(response_external, by_date=response_external.by_date[:2]),
        replace(response_external, by_date=response_external.by_date[3:])
    )
    assert get_daily(daily_data[0].date, daily_data[-1].date) == daily_data
    assert api_get.call_count == 2
    api_get.assert_has_calls((
        call(date(2017, 6, 12), date(2017, 6, 13)),
        call(date(2017, 6, 15), date(2017, 6, 15)),
    ))


def test_get_daily_with_invalid_dates():
    with raises(ValueError, match=r'older or equal'):
        get_daily(date(2020, 5, 12), date(2020, 5, 10))


def test_get_total(mocker, daily_data, total_data):
    get_daily = mocker.patch('cache.cache.get_daily')
    get_daily.return_value = daily_data
    assert get_total(daily_data[0].date, daily_data[-1].date) == total_data
    get_daily.assert_called_once_with(daily_data[0].date, daily_data[-1].date)


def test_get_total_with_invalid_dates():
    with raises(ValueError, match=r'older or equal'):
        get_total(date(2020, 5, 12), date(2020, 5, 10))
