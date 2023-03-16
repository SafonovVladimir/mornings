def cat_and_dog_years(cat_years: int, dog_years: int) -> list:
    cat = 0 if cat_years < 15 else 1 if cat_years < 24 else 2 + (
                cat_years - 24) // 4
    dog = 0 if dog_years < 15 else 1 if dog_years < 24 else 2 + (
                dog_years - 24) // 5
    return [cat, dog]


print(cat_and_dog_years(54, 64))  # повертає [10, 10]
