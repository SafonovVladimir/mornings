def jewels_and_stones(jewels: str, stones: str) -> int:
    return sum(stones.count(item) for item in set(list(jewels)))
