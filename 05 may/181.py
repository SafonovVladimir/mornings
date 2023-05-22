def accum(string: str) -> str:
    return "-".join([v.upper() + v * i for i, v in enumerate(string.lower())])


print(accum("aSdIy"))

# def maskify(card_number: str) -> str:
#     return f"{'#' * len(card_number[:-4])}{card_number[-4:]}"
#
# print(maskify("64607935616"))

# // maskify("64607935616") -> "#######5616"
