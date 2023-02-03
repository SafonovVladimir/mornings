def middle_character(word: str) -> str:

    if len(word) % 2 == 1:
        middle_symbol_index = int((len(word) - 1) / 2)
        return word[middle_symbol_index]
    middle_symbol_index = int((len(word)) / 2)
    return word[middle_symbol_index - 1: middle_symbol_index + 1]


print(middle_character("test"))
print(middle_character("testing"))
print(middle_character("middle"))
