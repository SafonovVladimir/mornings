# def count_ones(left: int, right: int) -> int:
import math


def count(n: int) -> int:
    if n == 0:
        return 0
    x = int(math.log(n, 2))
    return x * 2 ** (x - 1) + n - 2 ** x + 1 + count(n - 2 ** x)


def count_ones(left: int, right: int) -> int:
    return int(count(right) - count(left - 1))


print(count_ones(4, 7))  # повертає 8
print(count_ones(193303, 289384))  # повертає 916107
# 4(dec) == 100(bin), що додає 1 до результату.
# 5(dec) == 101(bin), що додає 2 до результату.
# 6(dec) == 110(bin), що додає 2 до результату.
# 7(dec) == 111(bin), що додає 3 до результату.
# Таким чином, підсумковий результат дорівнює 8.
