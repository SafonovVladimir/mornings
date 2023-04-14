from itertools import groupby


def count_and_say(number: int) -> str:
    string = "1"
    for i in range(number - 1):
        string = "".join(str(list(y).count(x)) + x for x, y in groupby(string))
    return string


# count_and_say(1)  # повертає "1"
print(count_and_say(10))  # повертає "1211" - Пояснення:
# countAndSay(1) = "1"
# countAndSay(2) = каже "1" = одна 1 = "11"
# countAndSay(3) = каже "11" = дві 1 = "21"
# countAndSay(4) = каже "21" = одна 2 + одна 1 = "12" + "11" = "1211"
