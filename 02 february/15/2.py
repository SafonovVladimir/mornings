from datetime import date


def unlucky_days(year: int) -> int:
    # count = 0
    # for day in range(1, 13):
    #     if date(year, day, 13).weekday() == 4:
    #         count += 1
    return sum(1 for day in range(1, 13) if date(year, day, 13).weekday() == 4)


print(unlucky_days(2015))
print(unlucky_days(1986))