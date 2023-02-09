from sys import getsizeof

def buy_and_sell_stock(prices: list) -> int:
    result_list = set()
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            result_list.add(prices[i])
            result_list.add(prices[i + 1])
    if not result_list:
        return 0
    result = max(sorted(result_list)) - min(sorted(result_list))
    size = getsizeof(result)
    return result, size


print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))# == 5 # День покупки – 2 (ціна = 1), день продажу – 5 (ціна = 6), прибуток = 6 - 1 = 5.

print(buy_and_sell_stock([7, 6, 4, 3, 1]))# == 0 # У цьому випадку, немає ніяких угод і прибуток = 0.
