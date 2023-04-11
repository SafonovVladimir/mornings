def shoot(results: list) -> str:
    p1_point = 0
    p2_point = 0

    for i in results:
        if i[1]:
            point = 2
        else:
            point = 1

        for key, value in i[0].items():
            if key == "P1":
                p1_point += value.count("X") * point
            else:
                p2_point += value.count("X") * point

    if p1_point > p2_point:
        return "Pete Wins!"
    if p2_point > p1_point:
        return "Phil Wins!"
    return "Draw!"


# results = [
#     [{"P1": "XX", "P2": "XO"}, True],
#     [{"P1": "OX", "P2": "OO"}, False],
#     [{"P1": "XX", "P2": "OX"}, True]
# ]
# print(shoot(results))  # повертає "Pete Wins!"
#
# results = [
#     [{"P1": "XX", "P2": "XO"}, False],
#     [{"P1": "OX", "P2": "XX"}, False],
#     [{"P1": "OO", "P2": "XX"}, True]
# ]
# print(shoot(results))  # повертає "Phil Wins!"

results = [
    [{"P1": "OO", "P2": "XX"}, False],
    [{"P1": "OO", "P2": "XX"}, False],
    [{"P1": "XX", "P2": "OO"}, True]
]
print(shoot(results))  # повертає "Draw!"
