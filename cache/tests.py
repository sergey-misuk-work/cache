from dataclasses import replace
from datetime import date
from django.core.cache import cache
from .views import daily, total


def test_daily_endpoint(request_factory, daily_data, daily_response, response_external, mocker):
    cache.clear()
    cache.set(str(date(2017, 6, 14)), daily_data[2])
    api_get = mocker.patch('cache.cache.get')
    api_get.side_effect = (
        replace(response_external, by_date=response_external.by_date[:2]),
        replace(response_external, by_date=response_external.by_date[3:])
    )
    query = {
        'start_date': daily_data[0].date,
        'end_date': daily_data[-1].date,
    }
    assert daily(request_factory.get('cache/daily', data=query)).data == daily_response


def test_total_endpoint(request_factory, daily_data, total_response, response_external, mocker):
    cache.clear()
    cache.set(str(date(2017, 6, 14)), daily_data[2])
    api_get = mocker.patch('cache.cache.get')
    api_get.side_effect = (
        replace(response_external, by_date=response_external.by_date[:2]),
        replace(response_external, by_date=response_external.by_date[3:])
    )
    query = {
        'start_date': daily_data[0].date,
        'end_date': daily_data[-1].date,
    }
    assert total(request_factory.get('cache/total', data=query)).data == total_response
