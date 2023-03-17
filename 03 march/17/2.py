def roman_to_int(roman: str) -> int:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    for i in range(len(roman) - 1, -1, -1):
        if 3 * roman_dict[roman[i]] < result:
            result -= roman_dict[roman[i]]
        else:
            result += roman_dict[roman[i]]
    return result

# print(roman_to_int("III"))# == 3
# print(roman_to_int("LVIII"))# == 58
print(roman_to_int("MCMXCIV"))# == 1994
