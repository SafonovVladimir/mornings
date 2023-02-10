def shortest_word(sentence: str) -> int:
    return min(len(word) for word in sentence.split(" "))

print(shortest_word("Mate Academy"))# == 4

print(shortest_word("Two ambitious students"))# == 3
