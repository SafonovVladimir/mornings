def highest_and_lowest(string_of_nums: str) -> str:
    return " ".join((max(string_of_nums.split()), min(string_of_nums.split())))

print(highest_and_lowest("1 2 3 4 5"))#  == "5 1"
print(highest_and_lowest("1 2 -3 4 5"))# == "5 -3"
print(highest_and_lowest("1 9 3 4 -5"))# == "9 -5"

