# def countLargestGroup(n: int) -> int:
#     result = []
#     arr = [i for i in range(1, n + 1)]
#     for i in arr:
#         if len(str(i)) > 1:
#             sum_num = sum(int(j) for j in str(i))
#             if sum_num in arr:
#                 result.append([sum_num, i])
#         else:
#             result.append([i])
#
#     print(result)
#     return len([i for i in result if len(i) == max(len(i) for i in result)])
#
#
# n = 24
# print(countLargestGroup(n))


a = "ADS;werwer;xcv;wwer;sdfqr;cvbf;rtu;fghgj;ert;dfg;rey"
b = "sdgf;asdg;werqw;xc;asdf;qwet;fvbfg;rtyu;saf;wrrwe;sdf"

# dict1 = {}
# for i in range(len(a.split(";"))):
#     dict1[a.split(";")[i]] = b.split(";")[i]

# a = a.split(";")
# b = b.split(";")
# print(dict(zip(a, b)))

def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(n) for n in range(8)])

