def descending_order(num_value: int) -> int:
    # for i in str(num_value)
    return int("".join(sorted(str(num_value), reverse=True)))

print(descending_order(42145))# == 54421

print(descending_order(123456789))# == 987654321
