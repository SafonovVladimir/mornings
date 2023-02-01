def perfect_number(number: int) -> bool:
    if number % 2 != 0:
        return False

    for i in range(number):
        if ((2 ** (i - 1)) * ((2 ** i) - 1)) == number:
            return True

    return False


print(perfect_number(137438691311))
