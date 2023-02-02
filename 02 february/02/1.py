def multiples_3_5(number: int) -> int:
    if number < 0:
        return 0

    return sum([i for i in range(number) if (i % 3 == 0 or i % 5 == 0)])


print(multiples_3_5(4))
print(multiples_3_5(15))