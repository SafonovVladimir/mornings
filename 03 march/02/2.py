def sum_of_squares(number: int) -> int:
    result = 0

    for i in range(number+1):
        coef = 1
        for j in range(i):
            coef *= number - j
            coef //= j + 1

        result += coef**2

    return result


n = 4
print("Sum of all elements:", sum_of_squares(n))
