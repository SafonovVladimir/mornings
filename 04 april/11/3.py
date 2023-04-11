def max_increase(grid: list) -> int:
    n = len(grid)
    row_max = [max(row) for row in grid]  # максимальні висоти на кожному рядку
    col_max = [max(col) for col in
               zip(*grid)]  # максимальні висоти на кожному стовпці
    result = 0
    for i in range(n):
        for j in range(n):
            result += min(row_max[i], col_max[j]) - grid[i][j]
    return result