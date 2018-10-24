from calendars.business_days import *
from calendars.country_calendars import *

business_day_services = {
    'UK': PandasBusinessDaysService(CustomBusinessDay(calendar=EnglandAndWalesHolidayCalendar())),
    'NL': PandasBusinessDaysService(CustomBusinessDay(calendar=NetherlandsBusinessCalendar()))
}


def latest_business_day(*args, **kwargs):
    country = kwargs.pop('country').upper()
    countries = list(business_day_services.keys())
    if country not in countries:
        raise ValueError(f'Not supported country! Currently supported = {",".join(countries)}')
    service = business_day_services[country]
    return service.latest_business_day(**kwargs)
