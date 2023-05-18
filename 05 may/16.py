def create_dict(list_1: list, list_2: list) -> dict:
    return {list_1[i]: list_2[i] for i in range(len(a))}


def replace_keys_and_values(a: dict) -> dict:
    return {value: key for key, value in a.items()}


def create_one_list(l: list) -> list:
    return [num for el in l for num in el]


def found_data(a: list, b: list) -> list:
    a_set = set(a)
    b_set = set(b)
    return list(a_set.intersection(b_set))


def max_value(d: dict) -> list:
    result_list = []

    three_highter_value = sorted(d.values())[-3:]

    for num in three_highter_value:
        for key, value in d.items():
            if value == num and key not in result_list:
                result_list.append(key)

    return result_list


# a = [1, 2, 3]
# b = ["q", "w", "e"]
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = {1: "value1", 2: "value2"}
# d = [[1, 2, 3], [4, 5, 6]]

# print(create_dict(a, b))
# print(replace_keys_and_values(c))
# print(create_one_list(d))
print(found_data(a, b))
d = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(max_value(d))
