from rest_framework.test import APIRequestFactory
from pytest import raises
from .views import daily
from datetime import date


def test_daily(daily_data, daily_response, mocker):
    factory = APIRequestFactory()
    start = date(2017, 6, 12)
    end = date(2017, 6, 15)
    query = {
        'start_date': start,
        'end_date': end,
    }
    cache_get = mocker.patch('cache.views.get_daily')
    cache_get.return_value = daily_data
    response = daily(factory.get('cache/daily', data=query))
    assert response.data == daily_response
    cache_get.assert_called_once_with(start, end)


def test_daily_with_invalid_dates(daily_response, mocker):
    factory = APIRequestFactory()
    start = date(2017, 6, 15)
    end = date(2017, 6, 12)
    query = {
        'start_date': start,
        'end_date': end,
    }
    with raises(ValueError, match=r' older or equal'):
        daily(factory.get('cache/daily', data=query))
