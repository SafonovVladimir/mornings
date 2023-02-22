def convert_the_score(score_string: str) -> list:
    score_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return [score_dict.get(word) for word in score_string.split() if word in score_dict.keys()]

print(convert_the_score("The score is four zero"))# == [4, 0]
print(convert_the_score("new score: two three"))# == [2, 3]
print(convert_the_score("two two"))# == [2, 2]
