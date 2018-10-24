from datetime import datetime

from behave import given, when, then
from nose.tools import assert_equal

from calendars.services import latest_business_day


@given(u'country id equals to {country}')
def step_impl(context, country):
    context.country = country


@given(u'current day is today')
def step_impl(context):
    context.current_date = datetime.today()


@given(u'current day is {current_date}')
def step_impl(context, current_date):
    context.current_date = current_date


@given(u'shifted days are {shifted_days}')
def step_impl(context, shifted_days):
    context.shifted_days = shifted_days


@when(u'get latest business days')
def step_impl(context):
    kwargs = {'country': context.country, 'current_date': context.current_date, 'shifted_days': context.shifted_days}
    context.latest_business_day = latest_business_day(**kwargs)


@then(u'latest business day is {expected_date}')
def step_impl(context, expected_date):
    assert_equal(expected_date, context.latest_business_day)
