def fix_string_case(word: str) -> str:
    count_lower = 0
    count_upper = 0

    for char in word:
        if char.islower() or char.isdigit() or char.isspace():
            count_lower += 1
        else:
            count_upper += 1

    print(count_lower)
    print(count_upper)

    if count_upper > count_lower:
        return word.upper()
    return word.lower()


# print(fix_string_case("coDe"))# = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# print(fix_string_case("CODe"))# = "CODE". Uppercase characters > lowercase. Change only the "e" to uppercase.
# print(fix_string_case("oUAEi"))# = "code". Uppercase == lowercase. Change all to lowercase.
print(fix_string_case("f  jj  MM A"))# = "code". Uppercase == lowercase. Change all to lowercase.
