def find_it(integers: list) -> int:
    for i in integers:
        if not integers.count(i) % 2:
            return i


