def discover_original_price(
    discounted_price: float, sale_percentage: float
) -> float:
    return round(discounted_price / (100 - sale_percentage) * 100, 2)

print(discover_original_price(75.00, 25.00))  # повертає 100.00
print(discover_original_price(2.00, 50.00))  # повертає 4.00
print(discover_original_price(55.00, 21.30))  # повертає 69.89
print(discover_original_price(458.20, 17.13))  # повертає 552.91
