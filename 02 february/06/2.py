def fibonacci_number(num_index: int) -> int:
    a, b = 0, 1
    for i in range(num_index):
        a, b = b, a + b
    return a


print(fibonacci_number(39))

