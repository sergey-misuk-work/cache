from datetime import date, timedelta
from django.core.cache import cache
from operator import attrgetter
from typing import List
from .api import get
from .data import SingleDay, TotalResponse
from .utils import date_range


def get_daily(start: date, end: date) -> List[SingleDay]:
    if start > end:
        raise ValueError('Start date must be older or equal to end date')

    dates = {
        i: cache.get(str(i))
        for i in date_range(start, end + timedelta(1))
    }

    missing = []
    fetched = []
    for k, v in dates.items():
        if v is not None:
            if missing:
                response = get(missing[0], missing[-1]) if len(missing) > 1 else get(missing[0], missing[0])
                fetched.extend((datum.to_single_day() for datum in response.by_date))
            missing = []
        else:
            missing.append(k)

    if missing:
        response = get(missing[0], missing[-1]) if len(missing) > 1 else get(missing[0], missing[0])
        fetched.extend((datum.to_single_day() for datum in response.by_date))

    for datum in fetched:
        dates[datum.date] = datum

    dates = {
        k: v
        for k, v in dates.items()
        if v is not None
    }

    for k, v in dates.items():
        cache.set(str(k), v)

    return list(dates.values())


def get_total(start: date, end: date) -> TotalResponse:
    if start > end:
        raise ValueError('Start date must be older or equal to end date')

    daily = get_daily(start, end)

    return TotalResponse(
        conversation_count=sum(map(attrgetter('conversation_count'), daily)),
        missed_chat_count=sum(map(attrgetter('missed_chat_count'), daily)),
        visitors_with_conversation_count=sum(map(attrgetter('visitors_with_conversation_count'), daily)),
    )
