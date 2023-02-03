def duplicate_encoder(word: str) -> str:
    lower_word = word.lower()
    return "".join([")" if lower_word.count(symbol) > 1 else "(" for symbol in lower_word])

# print(duplicate_encoder("din"))# == "((("
print(duplicate_encoder("recede"))# == "()()()"
# print(duplicate_encoder("Success"))# == ")())())"
# print(duplicate_encoder("(( @"))# ==  "))(("



