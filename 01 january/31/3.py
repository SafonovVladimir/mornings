from itertools import permutations

x = '531'


def next_smaller(number: int) -> int:
    str_number = str(number)
    perm = []
    for i in range(1, len(str_number) + 1):
        for c in permutations(str_number, i):
            if len(c) == len(str_number):
                perm.append("".join(c))

    if len(perm) <= 1:
        return -1

    sorted_perm = sorted(perm)
    for i in range(len(perm)):
        result = int(sorted_perm[i])
        if result == number:
            if int(sorted_perm[0]) == result:
                return -1
            if sorted_perm[i - 1][0] == "0":
                return -1
            return int(sorted_perm[i - 1])


print(next_smaller(531))
print(next_smaller(21))
print(next_smaller(2071))
print(next_smaller(9))
print(next_smaller(135))
print(next_smaller(1027))
