import json

import requests
from pandas import bdate_range
from pandas.tseries.holiday import *
from pandas.tseries.offsets import CustomBusinessDay


class BusinessDaysService(object):
    DATE_FORMAT = u'%Y-%m-%d'

    @classmethod
    def safe_date(cls, date):
        return date if isinstance(date, datetime) else datetime.strptime(date, cls.DATE_FORMAT)

    def latest_business_day(self, current_date=datetime.today(), shifted_days=1):
        raise NotImplementedError

    def business_day_in_range(self, from_date, to_date):
        raise NotImplementedError


class PandasBusinessDaysService(BusinessDaysService):
    def __init__(self, calendar=CustomBusinessDay()):
        self.calendar = calendar

    def latest_business_day(self, current_date=datetime.today(), shifted_days=1):
        today = self.safe_date(current_date)
        offset = self.calendar
        latest_business_day = today - int(shifted_days) * offset
        return latest_business_day.strftime(self.DATE_FORMAT)

    def business_day_in_range(self, from_date, to_date):
        start = self.safe_date(from_date)
        end = self.safe_date(to_date)
        holidays = self.calendar.holidays
        business_days = bdate_range(start=start, end=end, holidays=holidays)
        return [day.srtftime(self.DATE_FORMAT) for day in business_days]


class RestClientBusinessDaysService(BusinessDaysService):
    def __init__(self, city_id):
        self.calendar_definition_url = 'http://apps.cardano.intranet/dates/v1/calendardefinitions/' + city_id
        self.shifted_dates_url = 'http://apps.cardano.intranet/dates/v1/shifteddates'

    def latest_business_day(self, current_date=datetime.today(), shifted_days=1):
        today = self.safe_date(current_date)
        calendar_definition = requests.get(self.calendar_definition_url).json()[0]
        last_business_day_request = {
            'startDate': today.strftime(self.DATE_FORMAT),
            'tenorChain': [{'Number': -1 * int(shifted_days), 'Type': 'BusinessDays'}],
            'calendarDefinition': calendar_definition
        }
        body = json.dumps(last_business_day_request)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.shifted_dates_url, body, headers=headers)
        latest_business_day = self.safe_date(response.json()[0])
        return latest_business_day.strftime(self.DATE_FORMAT)

    def business_day_in_range(self, from_date, to_date):
        raise NotImplementedError
