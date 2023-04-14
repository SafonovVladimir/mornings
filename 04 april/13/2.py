KEYBOARD = ["abcde123fghij456klmno789pqrst.@0uvwxyz_/| ",
                 "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/| ",
                 "^~?!'\"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡```_/| "]


def tv_remote(word: str) -> int:
    count = x = y = shift = 0

    def key_press(key):
        nonlocal count, y, x, shift
        char_index = KEYBOARD[shift].index(key)
        char_x, char_y = char_index % 8, char_index // 8
        dx = abs(char_x - x)
        dy = abs(char_y - y)
        count += min(dx, 8 - dx) + min(dy, 6 - dy) + 1
        x, y = char_x, char_y

    for char in word:
        while char not in KEYBOARD[shift]:
            key_press("|")
            shift = (shift + 1) % 3
        key_press(char)

    return count

words = "Too Easy?"
print(tv_remote(words))
