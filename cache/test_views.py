from rest_framework.test import APIRequestFactory
from .views import daily
from datetime import date


def test_daily(api_response, mocker):
    factory = APIRequestFactory()
    start = date(2017, 6, 12)
    end = date(2017, 6, 15)
    query = {
        'start_date': start,
        'end_date': end,
    }
    api_get = mocker.patch('cache.views.get')
    api_get.return_value = api_response
    response = daily(factory.get('cache/daily', data=query))
    assert response.data == api_response.to_dict()
    api_get.assert_called_once_with(start, end)
