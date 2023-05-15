def make_valley(arr: list[int]) -> list[int]:
    # result = []
    # sorted_arr = sorted(arr)
    #
    # for i in range(len(sorted_arr)):
    #     if i % 2 == 0:
    #         result.insert(0, sorted_arr[i])
    #     else:
    #         result.append(sorted_arr[i])
    #
    # if len(result) % 2 == 0:
    #     if sum(result[:len(result) // 2]) <= sum(result[len(result) // 2:]):
    #         return result[::-1]
    # else:
    #     if sum(result[:len(result) // 2]) <= sum(result[len(result) // 2 + 1:]):
    #         return result[::-1]
    # return result
    arr = sorted(arr, reverse = True)
    print(arr)
    # return arr[::2] + arr[1::2][::-1]
    return arr[1::2]

    # return result if result[0] >= result[-1] else result[::-1]


print(make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1])) # [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]
print(make_valley([20, 7, 6, 2])) # [20, 6, 2, 7]
print(make_valley([14, 10, 8])) # [14, 8, 10]
