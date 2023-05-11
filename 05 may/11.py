def fairCandySwap(aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
    totalAlice = sum(aliceSizes)
    totalBob = sum(bobSizes)

    aliceSet = set(aliceSizes)
    bobSet = set(bobSizes)

    if totalAlice > totalBob:
        # Iterate through Bob's candy box sizes
        for candy in bobSet:
            targetCandy = candy + (totalAlice - totalBob) // 2
            if targetCandy in aliceSet:
                return [targetCandy, candy]
    else:
        # Iterate through Alice's candy box sizes
        for candy in aliceSet:
            targetCandy = candy + (totalBob - totalAlice) // 2
            if targetCandy in bobSet:
                return [candy, targetCandy]

    # No exact match found, return an arbitrary pair
    return [aliceSizes[0], bobSizes[0]]


# aliceSizes = [1, 1]
# bobSizes = [2, 2]
# aliceSizes = [1, 2]
# bobSizes = [2, 3]
aliceSizes = [2]
bobSizes = [1, 3]
print(fairCandySwap(aliceSizes, bobSizes))
