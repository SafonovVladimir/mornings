def mumbling(string: str) -> str:
    result = ""
    for i in range(len(string)):
        result += string[i].title() + string[i].lower() * i + "-"

    return result[:-1]

print(mumbling("abcd"))
print(mumbling("cwAt"))# -> "C-Ww-Aaa-Tttt"


