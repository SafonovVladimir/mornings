def detect_capital(word: str) -> bool:
    # if word.isupper():
    #     return True
    # if word.islower():
    #     return True
    # if word[0].isupper():
    #     return True

    return word in [word.upper(), word.lower(), word.title()]


print(detect_capital("USA"))# is True
print(detect_capital("FlaG"))# is False
print(detect_capital("python"))# is True
