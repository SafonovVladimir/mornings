def dir_reduction(plan: list) -> list:
    result = []
    dirs = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    for i in plan:
        if result and result[-1] == dirs[i]:
            result.pop()
        else:
            result.append(i)

    return output
        # if plan[i] == "SOUTH" and plan[i + 1] == "NORTH":
        #     print("SN", plan)
        #     plan.remove(plan[i + 1])
        #     plan.remove(plan[i])
        #     print("SN", plan)
        #     return dir_reduction(plan)
        # if plan[i] == "WEST" and plan[i + 1] == "EAST":
        #     plan.remove(plan[i + 1])
        #     plan.remove(plan[i])
        #     print("WE", plan)
        #     return dir_reduction(plan)
        # if plan[i] == "EAST" and plan[i + 1] == "WEST":
        #     plan.remove(plan[i + 1])
        #     plan.remove(plan[i])
        #     print("WE", plan)
        #     return dir_reduction(plan)
    return plan


print(dir_reduction(["EAST", "EAST", "WEST", "NORTH", "WEST", "SOUTH",
                     "NORTH"]))  # # returns ['WEST']
# print(dir_reduction(["NORTH", "SOUTH"]))  # # returns []
# print(dir_reduction(["NORTH", "NORTH", "SOUTH", "SOUTH"]))  # # returns []
# print(dir_reduction(["NORTH", "WEST", "SOUTH",
#                      "EAST"]))  # # returns ["NORTH", "WEST", "SOUTH", "EAST"]
