def isomorphic_strings(first_string: str, second_string: str) -> bool:
    indexes_first = {}
    indexes_second = {}
    if len(first_string) != len(second_string):
        return False

    for i in range(len(first_string)):
        if first_string[i] not in indexes_first:
            indexes_first[first_string[i]] = [i]
        else:
            indexes_first.get(first_string[i]).append(i)

    for i in range(len(second_string)):
        if second_string[i] not in indexes_second:
            indexes_second[second_string[i]] = [i]
        else:
            indexes_second.get(second_string[i]).append(i)

    x = list(indexes_first.values())
    y = list(indexes_second.values())

    return x == y



print(isomorphic_strings(first_string="egg", second_string="add"))# is True

print(isomorphic_strings(first_string="foo", second_string="bar"))# is False

print(isomorphic_strings(first_string="paper", second_string="title"))# is True
