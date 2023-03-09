def pascal_triangle_row(row_index: int) -> list:
    row = [1]
    for i in range(1, row_index + 1):
        row.append(int(row[i-1] * (row_index - i + 1) / i))
    return row


print(pascal_triangle_row(3))# == [1, 3, 3, 1]

print(pascal_triangle_row(0))# == [1]
