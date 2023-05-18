def binaryGap(n: int) -> int:
    n_list = []
    binary = bin(n)[2:]

    for i in range(len(binary)):
        if binary[i] == "1":
            n_list.append(i)
    if len(n_list) <= 1:
        return 0

    max_length = 0

    for i in range(len(n_list) - 1):
        max_length = max(max_length, int(n_list[i + 1]) - int(n_list[i]))
    return max_length


# n = 22
n = 13
# n = 6

print(binaryGap(n))
