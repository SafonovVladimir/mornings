def get_reversed_color(hex_color: str) -> str:
    hex_chars = "0123456789ABCDEF"

    if len(hex_color) > 6:
        raise ValueError

    for char in hex_color:
        if char.upper() not in hex_chars:
            raise ValueError

    result = "#"

    if len(hex_color) < 6:
        hex_color = hex_color.zfill(6)

    for char in hex_color:
        result += hex_chars[15 - hex_chars.find(char.upper())]

    return result


print(get_reversed_color("01fD08")) # повертає "#FE02F7"
print(get_reversed_color("")) # повертає "FFFFFF"
print(get_reversed_color("a23")) # повертає "#FFF5DC"
