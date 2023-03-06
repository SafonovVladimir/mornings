import copy


def tribonacci(signature: list, number: int) -> list:
    if number == 0:
        return []
    if number < 3:
        return [signature[i] for i in range(0, number)]
    res = copy.deepcopy(signature)
    for i in range(3, number):
        res.append(res[i - 1] + res[i - 2] + res[i - 3])
    return res
