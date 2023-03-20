def find_children(santas_list: list, children: list) -> list:
    return sorted([name for name in children if name in santas_list])


print(find_children(["Sam", "sAm", "saM"], ["Sam", "saM"]))  # повертає ["Sam", "saM"]
print(find_children(["jason", "Jackson", "jimmy", "Johny"], ["jackson", "Jimmy"]))  # повертає []
