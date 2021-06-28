from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .cache import get_daily, get_total
from datetime import datetime, date
from typing import Tuple

START = 'start_date'
END = 'end_date'
DATE_PARAMS = START, END
DATE_FORMAT = '%Y-%m-%d'


def _get_dates(request: Request) -> Tuple[date, date]:
    if not all(param in request.query_params for param in DATE_PARAMS):
        raise ValueError('Both start_date and end_date are required query parameters')
    return (datetime.strptime(request.query_params[START], DATE_FORMAT).date(),
            datetime.strptime(request.query_params[END], DATE_FORMAT).date())


@api_view(['GET'])
def daily(request: Request) -> Response:
    start, end = _get_dates(request)
    return Response([datum.to_dict() for datum in get_daily(start, end)])


@api_view(['GET'])
def total(request: Request) -> Response:
    start, end = _get_dates(request)
    return Response(get_total(start, end).to_dict())
