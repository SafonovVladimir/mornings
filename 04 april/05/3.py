from itertools import permutations, product


def equal_to_24(first_card: int, second_card: int, third_card: int,
                fouth_card: int) -> str:
    for first_card, second_card, third_card, fouth_card in permutations((
            first_card,
            second_card,
            third_card,
            fouth_card
    ), 4):
        for ops in product("+-*/", repeat=3):
            op1, op2, op3 = ops
            if op1 == op2 == op3 or all(op in "+-" for op in ops) or all(
                    op in "*/" for op in ops):
                expr = f"{first_card}{op1}{second_card}{op2}{third_card}{op3}{fouth_card}"
                if eval(expr) == 24:
                    return expr
                continue
            exprs = (
                f"{first_card}{op1}{second_card}{op2}{third_card}{op3}{fouth_card}",
                f"({first_card}{op1}{second_card}){op2}{third_card}{op3}{fouth_card}",
                f"({first_card}{op1}{second_card}{op2}{third_card}){op3}{fouth_card}",
                f"{first_card}{op1}({second_card}{op2}{third_card}){op3}{fouth_card}",
                f"{first_card}{op1}({second_card}{op2}{third_card}{op3}{fouth_card})",
                f"{first_card}{op1}{second_card}{op2}({third_card}{op3}{fouth_card})",
                f"({first_card}{op1}{second_card}){op2}({third_card}{op3}{fouth_card})",
            )
            for expr in exprs:
                try:
                    if eval(expr) == 24:
                        return expr
                except Exception:
                    pass
    return "It's not possible!"


print(equal_to_24(1, 2, 3,
                  4))  # може повернути "(1 + 3) * (2 + 4)" або "1 * 2 * 3 * 4"
print(equal_to_24(2, 3, 4,
                  5))  # може повернути "(5 + 3 - 2) * 4" або "(3 + 4 + 5) * 2"
print(equal_to_24(3, 4, 5, 6))  # може повернути "(3 - 4 + 5) * 6"
print(equal_to_24(1, 1, 1, 1))  # повертає "It's not possible!"
print(equal_to_24(13, 13, 13, 13))  # повертає "It's not possible!"
