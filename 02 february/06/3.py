def shortest_step(goal_num: int) -> int:
    steps = 0
    start_num = 1
    # while goal_num > 1:
    #     if (int(goal_num) & 1 == 0):
    #         goal_num *= 0.5
    #         steps += 1
    #     else:
    #         goal_num += -1
    #         steps += 1
    # return steps
    while start_num < goal_num:
        # if start_num + 1 == goal_num or start_num * 2 == goal_num:
        #     steps += 1
        #     return steps
        # else:
        if (start_num + 1) * 2 < goal_num:
            start_num *= 2
            steps += 1
            print(f"Multi {start_num}")
        else:
            start_num += 1
            steps += 1
            print(f"Add {start_num}")
    return steps

# print(shortest_step(3))
print(shortest_step(12))
# print(shortest_step(6))
# print(shortest_step(12))
# goal_num = 11
# print(goal_num % 2 == 0)
# print(goal_num & 1 == 0)