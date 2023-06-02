def is_divisor_game(number: int) -> bool:
    results = [False, False]

    for i in range(2, number + 1):
        for x in range(1, i):
            if i % x == 0 and not results[i - x]:
                results.append(True)
                break
        else:
            results.append(False)
    print(results)
    return results[number]

number = 100
print(is_divisor_game(number))
