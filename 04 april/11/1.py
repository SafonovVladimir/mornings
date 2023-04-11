def is_happy(number: int) -> bool:
    result = set()
    while number > 1 and number not in result:
        result.add(number)
        number = sum(int(d)**2 for d in str(number))
    return number == 1



print(is_happy(19))  # повертає True -
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1
print(is_happy(2))  # повертає False

