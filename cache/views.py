from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .api import get
from datetime import datetime

START = 'start_date'
END = 'end_date'
DATE_PARAMS = START, END
DATE_FORMAT = '%Y-%m-%d'


@api_view(['GET'])
def daily(request: Request) -> Response:
    if not all(param in request.query_params for param in DATE_PARAMS):
        raise ValueError('Both start_date and end_date are required query parameters')
    start = datetime.strptime(request.query_params[START], DATE_FORMAT).date()
    end = datetime.strptime(request.query_params[END], DATE_FORMAT).date()
    return Response(get(start, end).to_dict())
