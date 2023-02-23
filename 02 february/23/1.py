def two_to_one(first_str: str, second_str: str) -> str:
    return "".join(sorted(list(set(first_str + second_str))))


print(two_to_one("abcde", "ABCDE"))# == "ABCDEabcde"
print(two_to_one("xyaabbbccccdefww", "xxxxyyyyabklmopq"))# == "abcdefklmopqwxy"
