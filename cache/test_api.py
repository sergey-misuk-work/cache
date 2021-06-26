from .api import get
from .data import APIResponse
from datetime import date
from django.conf import settings
import pytest


def test_successful_get(raw_api_response, api_response, requests_mock):
    start = date(2017, 6, 12)
    end = date(2017, 6, 15)
    query = f'start_date={start}&end_date={end}'
    url = f'{settings.API_URL}?{query}'
    headers = {
        'Authorization': f'Token {settings.ACCESS_TOKEN}',
    }
    requests_mock.get(url, headers=headers, complete_qs=True, text=raw_api_response)
    data = get(start, end)
    assert data == api_response


def test_invalid_date_range():
    with pytest.raises(ValueError, match=r"older or equal"):
        start = date(2017, 6, 15)
        end = date(2017, 6, 12)
        get(start, end)
