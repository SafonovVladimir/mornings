from typing import List


def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    rotate_matrix = []

    for i in range(len(matrix[0])):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])

        rotate_matrix.append(column)
    result = []
    for i in range(len(rotate_matrix[0])):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(rotate_matrix[j]):
                result.append(matrix[i][j])
    return result if result else []
    # return [max([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == min(matrix[i]) else []])]


# matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
# matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
# matrix = [[7, 8], [1, 2]]
matrix = [[3, 6], [7, 1], [5, 2], [4, 8]]
print(luckyNumbers(matrix))
