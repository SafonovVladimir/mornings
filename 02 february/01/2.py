def sum_of_digits(number: int) -> int:
    if number == 0:
        return 0
    result = sum([int(i) for i in str(number)])

    if 0 < result < 10:
        return result
    else:
        return sum_of_digits(result)

print(sum_of_digits(0))
print(sum_of_digits(16))
print(sum_of_digits(942))
print(sum_of_digits(132189))

# while number > 9:
#     number = sum(map(int, str(number)))
# return number
