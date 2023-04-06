def scramble(first_string: str, second_string: str) -> bool:
    for char in second_string:
        if char not in first_string:
            return False
    else:
        return True

print(scramble("rkqodlw", "world"))  # повертає True
print(scramble("cehdewanpsoqqyt", "python"))  # повертає True
print(scramble("kartasc", "steak"))  # повертає False
