def ugly_numbers(num: int) -> bool:

    for i in [2, 3, 5]:
        while num % i == 0:
            num /= i
    return num == 1


print(ugly_numbers(2980))  # == True # 6 = 2 * 3
print(ugly_numbers(
    1))  # == True # 1 не містить простих множників, тому задовольняє умові
print(ugly_numbers(
    14))  # == False # 14 – не потворне число, оскільки воно містить простий множник 7
