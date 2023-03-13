def find_smallest(lst: list, number: int) -> list:
    sort_min_set = set(sorted(lst)[:number])
    return [i for i in lst if i in sort_min_set][:number]