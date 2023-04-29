def is_valid_ip(ip_address: str) -> bool:
    return ip_address.count(".") == 3 and all(
        i.isdigit() and 0 <= int(i) <= 255 and str(int(i)) == i for i in
        ip_address.split('.'))


print(is_valid_ip("1.2.003.4"))


def is_happy(number):
    seen = set()
    while number not in seen:
        seen.add(number)
        number = sum(int(num) ** 2 for num in str(number))
    return number == 1


print(is_happy(19))
print(is_happy(2))

def cakes(recipe, available):
    amount_ingredient = []
    for ingredient in recipe:
        if ingredient not in available or available[ingredient] < recipe[ingredient]:
            return 0
        else:
            amount_ingredient.append(available[ingredient] // recipe[ingredient])
    return min(amount_ingredient)

    # return min(available.get(ing, 0) / recipe[ing] for ing in recipe)


print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
