from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        szs = [1 for _ in range(m * n)]
        ids = [i for i in range(m * n)]

        def find(var1):
            if ids[var1] == var1:
                return var1
            return find(ids[var1])

        def union(v1, v2):
            i1, i2 = find(v1), find(v2)
            big, small = (i1, i2) if szs[i1] > szs[i2] else (i2, i1)
            szs[big] += szs[small]
            ids[small] = ids[big]

        def idof(i, j):
            nonlocal m, n
            return i * n + j

        visited = set()

        def isvalid(i, j):
            nonlocal m, n
            return 0 <= i < m and 0 <= j < n and A[i][j] == 1 and (i, j) not in visited

        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def helper(i, j):
            nonlocal m, n
            if not isvalid(i, j):
                return
            visited.add((i, j))
            for d in ds:
                ni, nj = d[0] + i, d[1] + j
                if isvalid(ni, nj):
                    union(idof(i, j), idof(ni, nj))
                    helper(ni, nj)

        for i in range(m):
            helper(i, 0)
            helper(i, n - 1)

        for i in range(n):
            helper(0, i)
            helper(m - 1, i)

        tot = 0
        for i in range(m):
            for j in range(n):
                tot += 1 if A[i][j] == 1 else 0

        return tot - len(visited)
