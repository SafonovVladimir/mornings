def histogram(results: list) -> str:
    count = len(results)
    result = ""

    for i in range(len(results) - 1, - 1, -1):
        if results[i] != 0:
            result += f"{count}|{'#' * results[i]} {results[i] if results[i] > 0 else ''}\n"
        else:
            result += f"{count}|\n"
        count -= 1

    return f'"""{result}"""'


print(histogram([7, 3, 10, 1, 0, 5]))  # повертає
"""6|##### 5
5|
4|# 1
3|########## 10
2|### 3
1|####### 7
"""
