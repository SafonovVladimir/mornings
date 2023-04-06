def pendulum(lst: list) -> list:
    result = []
    sort_lst = sorted(lst)
    for i in range(len(sort_lst)):
        if i % 2:
            result.append(sort_lst[i])
        else:
            result.insert(0, sort_lst[i])

    return result