def unique_code(words: list) -> int:
    morse_code = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }
    # result_list = []
    # for word in words:
        # result = "".join([morse_code.get(char) for char in word if char in morse_code])
        # for char in word:
        #     if char in morse_code:
        #         result += morse_code.get(char)
    return len(set(["".join([morse_code.get(char) for char in word if char in morse_code]) for word in words]))
    # result_set = set(result_list)
    # return len(result_set)

print(unique_code(["abc", "efg", "zxc"]))
print(unique_code(["gin", "zen"]))

