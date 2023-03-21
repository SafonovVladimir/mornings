def cakes(recipe: dict, available: dict) -> int:
    min_cakes = {}

    for key, value in recipe.items():
        if key in available:
            min_cakes[key] = 0
            while value <= available[key]:
                available[key] -= value
                min_cakes[key] += 1
        else:
            break

    return min(min_cakes.values()) if min_cakes else 0




print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))  # повертає 2
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))  # повертає 0
