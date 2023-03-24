import re


def consonant_value(string: str) -> int:
    result = re.split("[a|e|i|o|u]", string)
    print(result)

    if result[0] == "":
        result = result[1:]

    if len(result) <= 1:
        return 0

    max_num = 0

    for char in result:
        sum_ord_symbols = 0
        for s in char:
            sum_ord_symbols += ord(s) - 96

        if max_num < sum_ord_symbols:
            max_num = sum_ord_symbols 

    return max_num


print(consonant_value("zodiacs")) #26
# print(consonant_value("strength")) #57
# print(consonant_value("catchphrase"))
# print(consonant_value("b"))
print(consonant_value("ab")) #0
print(consonant_value("abb")) #0