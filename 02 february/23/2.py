def coin_combination(cents: int) -> list:
    result = []
    coins_list = [1, 5, 10, 25]
    for i in range(len(coins_list) - 1, -1, -1):
        result.append(cents // coins_list[i])
        cents %= coins_list[i]

    return result[::-1]

print(coin_combination(6))# == [1, 1, 0, 0]
print(coin_combination(42))# == [2, 1, 1, 1]
print(coin_combination(100))# == [0, 0, 0, 4]
