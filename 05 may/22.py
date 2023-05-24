# from itertools import combinations, permutations
#
#
# def lemonadeChange(bills: list[int]) -> bool:
#     fives, tens = 0, 0
#     for i in bills:
#         if i == 5:
#             fives += 1
#         elif i == 10:
#             if fives > 0:
#                 tens += 1
#                 fives -= 1
#             else:
#                 return False
#         else:
#             if tens > 0 and fives > 0:
#                 tens -= 1
#                 fives -= 1
#             elif fives > 2:
#                 fives -= 3
#             else:
#                 return False
#     return True
#
#
# bills = [5, 5, 5, 10, 20]
# # bills = [5, 5, 10, 10, 20]
# print(lemonadeChange(bills))

def bubble_search(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


lst = [2, 1, 5, 3, 4]
print(bubble_search(lst))
