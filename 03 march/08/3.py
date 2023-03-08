from itertools import product, combinations


def choose_best_sum(limit: int, number_of_towns: int, list_of_distances: list) -> int:
    # def choose_best_sum(t, k, list):
    res = []
    max_res = []
    for comb in combinations(list_of_distances, number_of_towns):
        res.append(sum(comb))

    for i in res:
        if i <= limit:
            max_res.append(i)

    if len(max_res) == 0:
        return None

    return max(max_res)
