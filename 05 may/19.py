from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    # result_list = []
    # for i in range(len(matrix[0])):
    #     result_list.append([matrix[j][i] for j in range(len(matrix))])

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # [[1,4,7],[2,5,8],[3,6,9]]
# matrix = [[1, 2, 3], [4, 5, 6]]  # [[1,4],[2,5],[3,6]]
print(transpose(matrix))
