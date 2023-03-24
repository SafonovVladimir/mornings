def is_isogram(string: str) -> bool:
    return len(string.lower()) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"))  # повертає True
print(is_isogram("aba"))  # повертає False
print(is_isogram("moOse"))  # повертає False
