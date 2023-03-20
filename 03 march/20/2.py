import re

def longest_vowel_chain(string: str) -> int:

    return max(len(i) for i in re.split("[^a|^e|^i|^o|^u]", string))


# print(longest_vowel_chain("codewarriors"))  # повертає 2 - найдовший ланцюжок io
# print(longest_vowel_chain("bestlessnesses"))  # повертає 1
print(longest_vowel_chain(
    "iiihoovaeaaaoougjyaw"))  # повертає 8 - найдовший ланцюжок aeaaaoou
# print(longest_vowel_chain("suoidea"))  # повертає 3
