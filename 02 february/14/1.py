def jaden_casing_strings(sentence: str) -> str:
    result_string = ""
    for word in sentence.split():
        new_word = word[0].title() + word.lower()[1:] + " "
        result_string += new_word
    return result_string[:-1]

print(jaden_casing_strings("How can mirrors be real if our eyes aren't real"))
# == "How Can Mirrors Be Real If Our Eyes Aren't Real"
# print(jaden_casing_strings("HOW ARE YOU?"))# == "How Are You?"
# print(jaden_casing_strings("aren't word"))# == "How Are You?"
