import requests
from django.conf import settings
from datetime import date
from .data import APIResponse


def get(start: date, end: date) -> APIResponse:
    if start > end:
        raise ValueError("Start date must be older or equal to end date")
    params = {
        'start_date': str(start),
        'end_date': str(end),
    }
    headers = {
        'Authorization': f'Token {settings.ACCESS_TOKEN}',
    }
    response = requests.get(settings.API_URL, params=params, headers=headers)
    return APIResponse.from_json(response.text)
