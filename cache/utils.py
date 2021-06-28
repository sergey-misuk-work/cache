from datetime import date, timedelta


def date_range(start: date, end: date):
    if start > end:
        raise ValueError('Start date must be older or equal to end date')
    yield from (start + timedelta(i) for i in range((end - start).days))
