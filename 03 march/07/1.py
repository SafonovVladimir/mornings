def count_primes(number: int) -> int:
    if number < 2:
        return 0

    primes = [True] * number
    primes[0] = primes[1] = False

    for i in range(2, int(number ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, number, i):
                primes[j] = False

    return sum(primes)


print(count_primes(10))# # returns 4 - there are 4 prime numbers less than 10, they are 2, 3, 5, 7.
print(count_primes(0))# # returns 0
print(count_primes(1))# # returns 0
