def dir_reduction(plan: list) -> list:
    result = []
    dirs = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    for i in plan:
        if result and result[-1] == dirs[i]:
            print(result, result[-1])
            result.pop()
        else:
            result.append(i)

    return result


print(dir_reduction(["EAST", "EAST", "WEST", "NORTH", "WEST", "SOUTH",
                     "NORTH"]))  # # returns ['WEST']
# print(dir_reduction(["NORTH", "SOUTH"]))  # # returns []
# print(dir_reduction(["NORTH", "NORTH", "SOUTH", "SOUTH"]))  # # returns []
# print(dir_reduction(["NORTH", "WEST", "SOUTH",
#                      "EAST"]))  # # returns ["NORTH", "WEST", "SOUTH", "EAST"]
