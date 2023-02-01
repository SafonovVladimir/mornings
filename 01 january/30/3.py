matrix = [[1, 2, 3],
          [8, 9, 4],
          [7, 6, 5]]


def snail(matrix: list) -> list:
    result_list = []

    while matrix:

        for item in matrix[0]:
            result_list.append(item)
        del matrix[0]

        if not matrix:
            break

        for j in matrix:
            result_list.append(j[-1])
            j.pop()

        for k in range(len(matrix[-1]) - 1, -1, -1):
            result_list.append(matrix[-1][k])
        matrix.pop()

        for m in reversed(matrix):
            result_list.append(m[0])
            del m[0]

    return result_list

print(snail(matrix))
