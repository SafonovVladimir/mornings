def length_of_last_word(string: str) -> int:
    print(string.split())
    return len(string.split()[-1])


print(length_of_last_word("Hello World"))  # повертає 5 - Останнє слово "World" має довжину 5
print(length_of_last_word("   fly me   to   the moon  "))  # повертає 4 - Останнє слово "moon" має довжину 4
print(length_of_last_word("luffy досі джойбою"))  # повертає 6 - Останнє слово "joyboy" має довжину 6
