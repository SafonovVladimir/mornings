def projectionArea(grid: list[list[int]]) -> int:
    projection_x = sum(max(i) for i in grid)
    projection_z = sum(j > 0 for i in grid for j in i)
    projection_y = sum(max(s[i] for s in grid) for i in range(len(grid)))

    return sum([projection_x, projection_y, projection_z])


grid = [[1, 2], [3, 4]]
# grid = [[1, 0], [0, 2]]
print(projectionArea(grid))
