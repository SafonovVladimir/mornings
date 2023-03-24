from itertools import chain


def dots_and_boxes(moves: tuple[int]) -> tuple[int]:
    nodes = 1 + max(sum(moves, ()))
    # nodes = 1 + max(chain.from_iterable(moves))
    player, y = 0, int(nodes ** 0.5)
    pts, grid = [0, 0], [4] * nodes
    for a, b in moves:
        swap = 1
        if a > b:
            a, b = b, a
        for i in (a, a - y if b - a == 1 else a - 1):
            if i < 0:
                continue
            grid[i] -= 1
            if not grid[i]:
                pts[player] += 1
                swap = 0
        player ^= swap
    return tuple(pts)


moves = (
    (0, 1), (7, 8), (1, 2), (6, 7), (0, 3), (8, 5), (3, 4), (4, 1), (4, 5),
    (2, 5),
    (7, 4), (3, 6))
print(dots_and_boxes(moves))  # поверає (3,1)
# moves = ((0, 1), (1, 2), (2, 5), (5, 4), (4, 7), (7, 8), (8, 5), (1, 4) , (6, 7), (3, 6), (3, 0), (3, 4))
# print(dots_and_boxes(moves))  # повертає (2, 2)
