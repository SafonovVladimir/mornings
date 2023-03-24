def pluck(dicts: list, name: str) -> list:
    # result = []
    # for diction in dicts:
    #     if name in diction.keys():
    #         result.append(diction[name])
    #     else:
    #         result.append(None)
    #
    # return result
    return [diction.get(name) for diction in dicts]


print(pluck([{'a':1}, {'a':2}], 'a'))  # повертає [1,2]
print(pluck([{'a':1, 'b':3}, {'a':2}], 'b'))  # повертає [3, None]
