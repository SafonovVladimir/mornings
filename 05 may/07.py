def findJudge(n: int, trust: list[list[int]]) -> int:
    trusts = {i: [] for i in range(1, n + 1)}
    trusted_by = {i: [] for i in range(1, n + 1)}

    for t in trust:
        trusts[t[1]].append(t[0])
        trusted_by[t[0]].append(t[1])
    print(trusts)
    print(trusted_by)

    for i, j in trusts.items():
        if len(j) == (n - 1) and len(trusted_by[i]) == 0:
            return i

    return -1


n = 3
trust = [[1, 3], [2, 3]]

print(findJudge(n, trust))
