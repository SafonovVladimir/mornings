def last_stone_weight(stones: list) -> int:
    while True:
        stones = sorted(stones, reverse=True)

        if len(stones) == 1:
            return stones[0]

        elif len(stones) == 0:
            return 0

        first = stones.pop(0)
        second = stones.pop(0)

        if first == second:
            continue

        else:
            stones.append(first - second)

    # stones.sort()
    #
    # while len(stones) > 1:
    #     y = stones.pop(-1)
    #     x = stones.pop(-1)
    #
    #     if x != y:
    #         stones.append(y - x)
    #     stones.sort()
    #
    #     return stones[0] if len(stones) >= 1 else 0

# stones = [2, 7, 4, 1, 8, 1]
stones = [1, 2, 3]

print(last_stone_weight(stones))



