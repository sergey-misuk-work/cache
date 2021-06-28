from datetime import date, timedelta
from django.core.cache import cache
from typing import List
from .api import get
from .data import DailyResponse
from .utils import date_range


def get_daily(start: date, end: date) -> List[DailyResponse]:
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
                fetched.extend((datum.to_daily_response() for datum in response.by_date))
            missing = []
        else:
            missing.append(k)

    if missing:
        response = get(missing[0], missing[-1]) if len(missing) > 1 else get(missing[0], missing[0])
        fetched.extend((datum.to_daily_response() for datum in response.by_date))

    print(dates)
    print(fetched)

    for datum in fetched:
        dates[datum.date] = datum

    print(dates)

    for k, v in dates.items():
        cache.set(str(k), v)

    return list(dates.values())
