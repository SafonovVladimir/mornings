def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


print(is_leap_year(4)) # повертає True
print(is_leap_year(100)) # повертає False
print(is_leap_year(400)) # повертає True
print(is_leap_year(1234)) # повертає False
