def find_smallest(arr: list, n: int) -> list:
    # sort_min_set = sorted(arr)[:n]
    # count_top = sort_min_set.count(sort_min_set[-1])
    # result = []
    #
    # for i in arr:
    #     if i <= sort_min_set[-1]:
    #         if i == sort_min_set[-1] and result.count(sort_min_set[-1]) < count_top:
    #             result.append(i)
    #         if i != sort_min_set[-1]:
    #             result.append(i)
    # return result[:n]
    keys = sorted(sorted(range(len(arr)), key=arr.__getitem__)[:n])
    return [arr[i] for i in keys]

lst = [17, 8, 17, 3, 14, 9, 7, 15, 15, 15, 14, 5, 2, 1, 18, 5, 3, 5, 1, 16, 20,
       18, 12, 16, 20, 10, 16, 8, 3, 20, 13, 12, 13, 7, 3, 3, 6, 16, 3, 5, 10,
       1, 12, 17, 8, 2, 18, 14, 3, 11, 1, 4, 19, 1, 2, 18, 4, 1, 9, 20, 20, 14,
       10, 4, 16, 8, 3, 15, 9, 10, 14, 6, 6, 8, 12, 6, 6, 14, 5, 1, 5, 16, 10,
       4, 7, 14, 4, 5, 11, 4, 16, 3, 4, 1, 3, 16, 13, 19, 10, 20]
result = [3, 2, 1, 3, 1, 3, 3, 3, 3, 1, 2, 3, 1, 4, 1, 2, 4, 1, 4, 3, 1, 4, 4,
          3, 1, 3]
# print(result)
print(find_smallest(lst, 26))
# print(find_smallest(lst, 26) == result)
