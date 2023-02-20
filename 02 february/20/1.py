def capitals_first(sentence: str) -> str:
    upper_words = []
    lower_words = []
    sentence = sentence.split()
    for i in range(len(sentence)):
        if sentence[i][0].isupper():
            upper_words.append(sentence[i])
        else:
            lower_words.append(sentence[i])

    upper_words.extend(lower_words)
    return " ".join(upper_words)


# print(capitals_first("z x c b Z Z X CC B"))# == "Mate academy"
print(capitals_first("z"))# == "Mate academy"
print(capitals_first("Q q"))# == "Mate academy"
print(capitals_first("abc Cba"))# == "Mate academy"
# print(capitals_first("one Two three Four"))# == "Two Four one three"
