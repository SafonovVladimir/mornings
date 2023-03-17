def count_nines(number: int) -> int:
    return sum(str(i).count("9") for i in range(number + 1))

print(count_nines(8))# # повертає 0
print(count_nines(9))# # повертає 1
print(count_nines(10))# # повертає 1
print(count_nines(98))# # повертає 18
print(count_nines(100))# # повертає 20
