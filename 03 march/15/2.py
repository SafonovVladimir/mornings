def climb_stairs(number: int) -> int:
    if number == 1 or number == 2:
        return number

    one_stair = 1
    two_stairs = 2
    current = 0

    for step in range(3, number + 1):
        current = one_stair + two_stairs
        one_stair = two_stairs
        two_stairs = current
    return current

