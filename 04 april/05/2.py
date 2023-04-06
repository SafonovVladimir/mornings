def reverse_integer(number: int) -> int:
    if number not in range(-2**31, 2**31 - 1):
        return 0

    result = ""
    str_number = str(number)

    if number < 0:
        result += "-"
        result += "".join(str_number[1:][::-1])

    else:
        result += "".join(str_number[::-1])

    return int(result)

print(reverse_integer(123))  # повертає 321
print(reverse_integer(-123))  # повертає -321
print(reverse_integer(120))  # повертає 21
