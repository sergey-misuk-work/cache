from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime
from django.views.decorators.cache import cache_page
from django.conf import settings


@cache_page(settings.CACHE_TTL)
@api_view(['GET'])
def daily(request: Request):
    return Response(datetime.now())
