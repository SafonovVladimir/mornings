def group_by_commas(number: int) -> str:
    result = list(str(number))
    for i in range(len(result), 0, -3):
        result.insert(i, ",")
    return "".join(result[:-1])

print(group_by_commas(100)) # повертає "100"
print(group_by_commas(1000)) # повертає "1,000"
print(group_by_commas(10000)) # повертає "10,000"
print(group_by_commas(100000)) # повертає "100,000"


