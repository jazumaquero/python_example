from pandas.tseries.holiday import *
from pandas.tseries.offsets import Day


class EnglandAndWalesHolidayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('New Years Day', month=1, day=1, observance=next_monday),
        GoodFriday,
        EasterMonday,
        Holiday('Early May bank holiday', month=5, day=1, offset=DateOffset(weekday=MO(1))),
        Holiday('Spring bank holiday', month=5, day=31, offset=DateOffset(weekday=MO(-1))),
        Holiday('Summer bank holiday', month=8, day=31, offset=DateOffset(weekday=MO(-1))),
        Holiday('Christmas Day', month=12, day=25, observance=next_monday),
        Holiday('Boxing Day', month=12, day=26, observance=next_monday_or_tuesday)
    ]


class NetherlandsBusinessCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('New Years Day', month=1, day=1, observance=next_monday),
        GoodFriday,
        EasterMonday,
        Holiday("King's Birthday", month=4, day=27, observance=next_monday),
        Holiday('Ascension Day', month=1, day=1, offset=[Easter(), Day(39)]),
        Holiday('Pentecost Day', month=1, day=1, offset=[Easter(), Day(50)]),
        Holiday('Whit Monday', month=12, day=25, offset=[Easter(), Day(51)]),
        Holiday('Boxing Day', month=12, day=26, observance=next_monday_or_tuesday)
    ]

