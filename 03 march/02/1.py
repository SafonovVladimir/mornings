def get_order(order: str) -> str:
    result = ""
    menu = ["Burger", "Fries", "Chicken", "Pizza", "Sandwich", "Onionrings", "Milkshake", "Coke"]

    for item in menu:
        if item.lower() in order:
            count = len(order.split(item.lower())) - 1
            result += (item + " ") * count
    return result[:-1]

# print(get_order("burgersandwich"))# # повертає "Burger Sandwich"
# print(get_order("cokefriessandwichpizzaburger")) # повертає "Burger Fries Pizza Sandwich Coke"
# print(get_order("pizzachickenfriesburgercokemilkshakefriessandwich")) # повертає "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"
print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")) # повертає "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
# print(get_order("milkshakemilkshakemilkshakemilkshake")) # повертає "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
