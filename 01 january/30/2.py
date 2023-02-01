def vowel_count(sentence: str) -> int:
    count = 0
    vowel = ["a", "e", "i", "o", "u"]

    for i in sentence:
        if i in vowel:
            count += 1

    return count

print(vowel_count("aei ou"))