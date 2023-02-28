import string


def convert_to_title(num: int) -> str:
    result = ""
    ascii_string = string.ascii_uppercase
    while num:
        char_from_ascii = (num-1) % 26
        num = int((num - char_from_ascii) / 26)
        result += ascii_string[char_from_ascii]
    return result[::-1]


print(convert_to_title(1)) # повертає "A" - заголовок першої колонки в Excel
# print(convert_to_title(2)) # повертає "B"
# print(convert_to_title(28)) # повертає "AB"
print(convert_to_title(701)) # повертає "ZY"
