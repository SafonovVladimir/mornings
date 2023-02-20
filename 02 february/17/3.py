def shorten_to_date(long_date: str) -> str:
    return long_date[:long_date.find(",")]

print(shorten_to_date("Wed September 1, 3am"))  # повертає "Wed September 1"
print(shorten_to_date("Tuesday January 29, 10pm"))  # повертає "Tuesday January 29"
