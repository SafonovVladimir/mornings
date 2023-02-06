def shortest_step(goal_num: int) -> int:
    steps = 0
    while goal_num > 1:
        if goal_num % 2 == 0:
            goal_num /= 2
            steps += 1
        else:
            goal_num -= 1
            steps += 1
    return steps

print(shortest_step(3))
print(shortest_step(12))
