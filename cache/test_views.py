from pytest import raises
from .views import daily, total
from datetime import date


def test_daily(request_factory, daily_data, daily_response, mocker):
    query = {
        'start_date': daily_data[0].date,
        'end_date': daily_data[-1].date,
    }
    cache_get = mocker.patch('cache.views.get_daily')
    cache_get.return_value = daily_data
    response = daily(request_factory.get('cache/daily', data=query))
    assert response.data == daily_response
    cache_get.assert_called_once_with(daily_data[0].date, daily_data[-1].date)


def test_daily_with_invalid_dates(request_factory):
    start = date(2017, 6, 15)
    end = date(2017, 6, 12)
    query = {
        'start_date': start,
        'end_date': end,
    }
    with raises(ValueError, match=r'older or equal'):
        daily(request_factory.get('cache/daily', data=query))


def test_total(request_factory, daily_data, total_data, total_response, mocker):
    query = {
        'start_date': daily_data[0].date,
        'end_date': daily_data[-1].date,
    }
    cache_get = mocker.patch('cache.views.get_total')
    cache_get.return_value = total_data
    response = total(request_factory.get('cache/total', data=query))
    assert response.data == total_response
    cache_get.assert_called_once_with(daily_data[0].date, daily_data[-1].date)


def test_total_with_invalid_dates(request_factory):
    start = date(2017, 6, 15)
    end = date(2017, 6, 12)
    query = {
        'start_date': start,
        'end_date': end,
    }
    with raises(ValueError, match=r'older or equal'):
        total(request_factory.get('cache/total', data=query))
