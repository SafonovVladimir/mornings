def all_inclusive(string: str, lst: list) -> bool:
    if not string:
        return True

    list_str = list(string)
    turns = []
    for i in range(len(list_str)):
        list_str.append(list_str[0])
        list_str.pop(0)
        turns.append("".join(list_str))

    return all([True if i in lst else False for i in turns])




print(all_inclusive("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"])) # повертає Тrue - список включає всі обороти
print(all_inclusive("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"])) # повертає False
# - оборот "yAjylvp" відсутній у списку

# print(all_inclusive("", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))