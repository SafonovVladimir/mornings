# # # dict1 = {1: "value1", 2: "value2"}
# # #
# # #
# # # def change_keys_and_values(dictionary: dict) -> dict:
# # #     return {v: k for k, v in dictionary.items()}
# # #
# # #
# # # print(change_keys_and_values(dict1))
# # #
# # #
# # # def dict_creator(list1: list, list2: list) -> dict:
# # #     if len(list1) != len(list2):
# # #         return dict()
# # #
# # #     return {list1[i]: list2[i] for i in range(len(list1))}
# # #
# # #
# # # a = [1, 2, 3]
# # # b = ["q", "w", "e"]
# # #
# # # print(dict_creator(a, b))
# # #
# # #
# # # def one_list_create(lst: list) -> list:
# # #     result = []
# # #     # for i in lst:
# # #     #     result.extend(i)
# # #     # return result
# # #
# # #     for i in lst:
# # #         for j in i:
# # #             result.append(j)
# # #
# # #     return result
# # #
# # #
# # # lst = [[1, 2, 3], [4, 5, 6]]
# # # print(one_list_create(lst))
# #
# # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# #
# # def get_similar_numbers(lst1: list, lst2: list) -> list:
# #     return list(set(a).intersection(set(b)))
# #
# # print(get_similar_numbers(a, b))
# # import json
# #
# # jsn = '{"1": "asd", "2": "sdfszdf"}'
# #
# # data = json.loads(jsn)
# #
# # print(data["1"])
# # print(data["2"])
#
# #
# # def bubble_search(lst: list) -> list:
# #     n = len(lst)
# #
# #     for i in range(n - 1):
# #         for j in range(n - 1 - i):
# #             if lst[j] > lst[j + 1]:
# #                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
# #
# #     return lst
# #
# #
# # lst = [4, 1, 2, 7, 3, 5]
# #
# # print(bubble_search(lst))
# import math
#
#
# class Sphere:
#     def square(self):
#         ...
#
# class Circle(Sphere):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def square(self):
#         return round(math.pi * self.radius ** 2, 2)
#
# class Rectangle(Sphere):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def square(self):
#         return self.width * self.height
#
# class Square(Sphere):
#     def __init__(self, side):
#         self.side = side
#
#     def square(self):
#         return self.side ** 2
#
#
# rectangle = Rectangle(4, 5)
# circle = Circle(5)
# square = Square(4)
#
# print(rectangle.square())
# print(circle.square())
# print(square.square())
#
#
def get_three_higher_values(dct: dict) -> list:
    three_higher_values = sorted(dct.values())[-3:]
    return [k for k, v in dct.items() if v in three_higher_values]

dct = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

print(get_three_higher_values(dct))

