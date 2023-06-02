def stringMatching(words: list[str]) -> list[str]:
    result = []
    for word in words:
        for sub_string in words:
            if len(sub_string) < len(word) and sub_string in word and sub_string not in result:
                result.append(sub_string)

    return result
    # return set([sub_string for word in words for sub_string in words if len(sub_string) < len(word) and sub_string in word and sub_string not in result])


# words = ["mass", "as", "hero", "superhero"]
words = ["leetcoder","leetcode","od","hamlet","am"]
print(stringMatching(words))
