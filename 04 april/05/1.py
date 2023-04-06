def one_down(txt: str) -> str:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    if not isinstance(txt, str):
        return "Input is not a string"

    result = ""

    for char in txt:
        if char == " ":
            result += " "
        else:
            if char.isupper():
                result += upper[upper.find(char) - 1]
            elif char.islower():
                result += lower[lower.find(char) - 1]

    return result


# print(one_down("Ifmmp"))  # повертає "Hello"
print(one_down("qVAamFt BsF gVo"))  # "pUZzlEs ArE fUn"
print(one_down("Mate Academy RockZ"))  # повертає "Hello"
# print(one_down(["Привіт", "Світ"]))  # повертає "Input is not a string"
print(one_down("XiBu BcPvU dSbAz UfYu"))  # повертає "WhAt AbOuT cRaZy TeXt"
