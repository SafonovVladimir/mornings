def max_redigit(num: int) -> int:
    if num <= 0:
        return None

    result = ""

    for i in sorted(str(num), reverse=True):
        result += i

    return int(result)

print(max_redigit(99)) # повертає None
# print(max_redigit(1000)) # повертає 321
# print(max_redigit(418)) # повертає 841
# print(max_redigit(999)) # повертає 999
