def square_every_digit(number: int) -> int:
    return int("".join([str((int(i) ** 2)) for i in str(number)]))



print(square_every_digit(9119))