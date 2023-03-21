def is_valid_ip(ip_address: str) -> bool:
    if len(ip_address.split(".")) != 4:
        return False

    for i in ip_address.split("."):
        try:
            int(i)
        except ValueError:
            return False

        if int(i) not in range(0, 256) or (i.startswith("0") and len(i) != 1) or i[-1].isspace():
            return False
    return True


print(is_valid_ip("abc.def.ghi.jkl")) # повертає True
# print(is_valid_ip("123.45.67.89")) # повертає True
# print(is_valid_ip("1.2.3")) # повертає False
# print(is_valid_ip("1.2.3.4.5")) # повертає False
# print(is_valid_ip("123.456.78.90")) # повертає False
# print(is_valid_ip("123.045.067.089")) # повертає False
