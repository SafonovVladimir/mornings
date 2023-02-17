def longest_gap(num_decimal: int) -> int:
    result = 0
    gap = 0

    for num in bin(num_decimal)[2:]:

        if num == "0":
            gap += 1
        else:
            if gap > result:
                result = gap
            gap = 0

    return result


print(longest_gap(529))
print(longest_gap(0))
print(longest_gap(2))
# print(bin(2))
