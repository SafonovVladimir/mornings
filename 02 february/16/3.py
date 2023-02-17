def buy_tofu(cost: int, box: str) -> list or str:
    count_of_mon_coins_in_box = 0
    count_of_monme_coins_in_box = 0

    for i in box.split():
        if i == "mon":
            count_of_mon_coins_in_box += 1
        if i == "monme":
            count_of_monme_coins_in_box += 1

    sum_of_all_coins_value_in_box = (
            count_of_mon_coins_in_box + count_of_monme_coins_in_box * 60)

    if cost > sum_of_all_coins_value_in_box:
        return "leaving the market"

    if count_of_monme_coins_in_box < count_coins(cost)[1] and count_of_mon_coins_in_box < (cost - count_of_monme_coins_in_box * 60):
        return "leaving the market"

    if count_coins(cost)[1] == 0 and count_of_mon_coins_in_box < count_coins(cost)[0]:
        return "leaving the market"

    if count_of_monme_coins_in_box < count_coins(cost)[1]:
        minimum_number_of_coins_needed_for_tofu = cost - count_of_monme_coins_in_box * 60 + count_of_monme_coins_in_box
    else:
        minimum_number_of_coins_needed_for_tofu = sum(count_coins(cost))

    return [count_of_mon_coins_in_box,
            count_of_monme_coins_in_box,
            sum_of_all_coins_value_in_box,
            minimum_number_of_coins_needed_for_tofu]


def count_coins(cost: int) -> list:
    coins_count_1 = 0
    coins_count_60 = 0

    if cost < 60:
        return [cost, 0]

    while cost % 60 != 0:
        cost -= 1
        coins_count_1 += 1

    else:
        coins_count_60 += cost / 60

    return [coins_count_1, int(coins_count_60)]


print(count_coins(5))
cost = 5
box = 'mon monme'
print(buy_tofu(cost, box))
# cost = 124
# box = 'mon mon mon mon mon apple mon mon mon mon mon mon mon monme mon mon monme mon mon mon mon cloth monme mon mon mon mon mon mon mon mon cloth mon mon monme mon mon mon mon monme mon mon mon mon mon mon mon mon mon mon mon mon mon'
# print(count_coins(124))
# cost = 124
# box = "mon mon mon mon mon apple mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon monme mon mon mon mon cloth mon mon mon mon mon mon mon mon mon cloth mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon"
# print(buy_tofu(cost, box))  # returns "leaving the market"

# cost = 122
# box = "monme pie mon mon apple monme"
# print(buy_tofu(cost, box))  # returns [2,2,122,4]
#
# cost = 674
# box = "mon mon mon"
# print(buy_tofu(cost, box))  # returns "leaving the market"
