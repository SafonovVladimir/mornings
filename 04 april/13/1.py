KEYBOARD = "abcde123fghij456klmno789pqrst.@0uvwxyz_/"


def tv_remote(word: str) -> int:
    count = x = y = 0

    for char in word:
        char_index = KEYBOARD.index(char)
        char_x, char_y = char_index % 8, char_index // 8
        count += abs(char_x - x) + abs(char_y - y) + 1
        x, y = char_x, char_y

    return count

    # count = x = y = 0
    #
    # for char in word:
    #     position = KEYBOARD.index(char)
    #     char_x, char_y = position % 8, position // 8
    #     count += abs(char_x - x) + abs(char_y - y) + 1
    #     x, y = char_x, char_y
    #
    # return count


print(tv_remote("c"))  # повертає 14:
print(tv_remote("code"))  # повертає 14:
# с => а-б-в-ОК = 3
# o => c-d-e-j-o-OK = 5
# d => o-j-e-d-OK = 4
# е => д-е-ОК = 2
# print(tv_remote("solution"))  # повертає 33
# print(tv_remote(""))  # повертає 0
# tv_remote("@_/0")  # повертає 16
