def number_of_deleted_columns(strings: list) -> int:
    final = []
    result = []
    for i in range(len(strings[0])):
        column = []
        for string in strings:
            column.append(string[i])
        result.append("".join(column))

    for i in result:
        final.append(i == "".join(sorted(i)))

    return final.count(False)



strings = ["cba", "daf", "ghi"]

print(number_of_deleted_columns(strings))