def find_sum(row, i):
    if i in (0, row):
        return 1
    return find_sum(row - 1, i - 1) + find_sum(row - 1, i)


def generate_rows(rows: int) -> list:
    result = []

    for row in range(rows):
        temp_result = []

        for i in range(row + 1):
            temp_result.append(find_sum(row, i))

        result.append(temp_result)

    return result

print(generate_rows(5))#  # повертає [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(generate_rows(1))#  # повертає [[1]]
