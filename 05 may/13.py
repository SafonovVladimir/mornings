def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    return list(set(s1.split()).symmetric_difference(set(s2.split())))


s1 = "this apple is sweet"
s2 = "this apple is sour"

print(uncommonFromSentences(s1, s2))
