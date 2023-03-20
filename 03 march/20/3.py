def compression(chars: list) -> int:
    result = []
    chars_temp = []
    count = 1

    for i in chars:
        if i in chars_temp:
            count += 1
        else:
            if count > 1:
                result.extend([i for i in str(count)])
            chars_temp = []
            chars_temp.append(i)
            result.append(i)
            count = 1

    if count > 1:
        result.extend([i for i in str(count)])

    return len(result)


# print(compression(["a", "a", "b", "b", "c", "c", "c"]))  # повертає 6 - новий список chars ["a", "2", "b", "2", "c", "3"]
# групи "aa", "bb" та "ccc" стискаються до "a2b2c3".
# print(compression(["a"]))  # повертає 1 - дина група - це "a", яка залишається не стиснутою, тому що це один символ.
# print(compression(["a", "b", "b"]))  # повертає 1 - дина група - це "a", яка залишається не стиснутою, тому що це один символ.
# print(compression([1, 1, 1, 2, 2, 3, 4, 4]))  # повертає 1 - дина група - це "a", яка залишається не стиснутою, тому що це один символ.
print(compression(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # повертає 4 - новий список символів ["a", "b", "1", "2"]
# групи "a" та "bbbbbbbbbbbbbb" стискаються до "ab12".
