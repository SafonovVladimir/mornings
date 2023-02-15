def longest_gap(num_decimal: int) -> int:
    hex_num = str(bin(num_decimal)[2:]).strip("0").split("1")
    return max(hex_num, key=lambda x: x.count("0")).count("0")


# print(longest_gap(529))
# print(longest_gap(0))
print(longest_gap(2))
# print(bin(2))
