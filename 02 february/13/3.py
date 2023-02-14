from functools import reduce


def chained(functions: list):
    def apply(param):
        result = param
        for f in functions:
            result = f(result)
        return result
    return apply
    # return lambda args: reduce(lambda result, f: f(result), functions, args)


def f1(x): return x * 2


def f2(x): return x + 2


def f3(x): return x ** 2


print(chained([f1, f2, f3])(0))  # => f3(f2(f1(0))) #повертає 4
# print(chained([f1,f2,f3])(2))# => f3(f2(f1(0))) #повертає 36
# print(chained([f3,f2,f1])(2))# => f1(f2(f3(0))) #повертає 12
