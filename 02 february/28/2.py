def reverse_random_string(random_string: str, amount_of_symbols: int) -> str:
    lenght = len(random_string)

    if lenght < amount_of_symbols:
        return random_string[::-1]

    if lenght < 2 * amount_of_symbols and lenght >= amount_of_symbols:
        return (random_string[:amount_of_symbols][::-1]
                + random_string[amount_of_symbols:])

    add_interval = amount_of_symbols * 2
    return (random_string[:amount_of_symbols][::-1]
            + random_string[amount_of_symbols:add_interval]
            + random_string[add_interval:add_interval + amount_of_symbols][::-1]
            + random_string[add_interval + amount_of_symbols:])

# Input: random_string = "abcdefg", amount_of_symbols = 2
# Output: "bacdfeg"
print(reverse_random_string("abcdefg", 2))