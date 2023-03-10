def who_likes_it(names: list) -> str:
    if len(names) == 0:
        return f"no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    if len(names) >= 4:
        return f"{names[0]}, {names[1]}, and {len(names) - 2} others like this"

print(who_likes_it([]))# == "no one likes this"
print(who_likes_it(["Peter"]))# == "Peter likes this"
print(who_likes_it(["Jacob", "Alex"]))# == "Jacob and Alex like this"
print(who_likes_it(["Max", "John", "Mark"]))# == "Max, John and Mark like this"
print(who_likes_it(["Alex", "Jacob", "Mark", "Max"]))# == "Alex, Jacob and 2 others like this"

