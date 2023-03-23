def find_needed_guards(islands: list) -> int:
    count_guards = 0
    for i in range(len(islands) - 1):
        if islands[i] is False and islands[i + 1] is False:
            count_guards += 1
            islands[i + 1] = True
    return count_guards

print(find_needed_guards([True, True, False, True, False]))  # повертає 0
print(find_needed_guards([False, False, True, False, False]))  # повертає 2
print(find_needed_guards([False, False, True, False, True, False, False, False, False]))  # повертає 3
