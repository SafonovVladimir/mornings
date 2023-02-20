import datetime


def calendar_week(date_string: str) -> int:
    year, month, day = date_string.split("-")
    return datetime.date(int(year), int(month), int(day)).isocalendar()[1]



print(calendar_week("2019-01-01"))# == 1

print(calendar_week("2016-02-29"))# == 9
