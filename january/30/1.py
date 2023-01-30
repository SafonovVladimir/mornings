def data_compression(data: str) -> str:
    result = ""
    i = 0

    while i <= len(data) - 1:
        count = 1
        char = data[i]
        j = i
        while j < len(data) - 1:
            if data[j] == data[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        result += str(count) + char
        i = j + 1

    return result
