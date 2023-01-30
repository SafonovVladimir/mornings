def data_compression(data: str) -> str:
    uniq_data = ""

    for i in data:
        if i not in uniq_data:
            uniq_data += i

    return "".join([(str(data.count(j)) + j) for j in uniq_data])

print(data_compression("AAABBBCCCD"))
