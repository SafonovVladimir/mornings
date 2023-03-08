def sum_of_a_sequence(begin_number: int, end_number: int, step: int) -> int:
    if end_number < begin_number:
        return 0

    return sum(i for i in range(begin_number, end_number + 1, step))

print(sum_of_a_sequence(begin_number=1, end_number=5, step=3))# == 28 # 1 + 2 + 3 + 4 + 5 + 6 + 7

# print(sum_of_a_sequence(begin_number=2, end_number=6, step=2))# == 12 # 2 + 4 + 6

# print(sum_of_a_sequence(begin_number=9, end_number=3, step=3))# == 0
