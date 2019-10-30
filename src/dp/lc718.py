from typing import List
from functools import lru_cache


class Solution2:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        bmap = {}
        for i, b in enumerate(B):
            if b not in bmap.keys():
                bmap[b] = []  # value to index mapping
            bmap[b].append(i)

        @lru_cache(None)
        def dp(i, j):  # given A[i:] and B[j:] and a[i] == b[j] what's the longest suffix?
            nonlocal m, n
            if i + 1 < m and j + 1 < n and A[i + 1] == B[j + 1]:
                return dp(i + 1, j + 1) + 1
            return 1

        maxlen = 0
        # for i in range(m - 1, -1, -1):
        for i in range(m):
            if m - i < maxlen:
                continue
            a = A[i]
            bmj = bmap.get(a, [])
            for j in range(len(bmj) - 1, -1, -1):  # worst case here still O(mn)
                k = bmj[j]
                if i + maxlen >= k:  # j is decreasing, if the matching already past self, then move on
                    break
                if dp(i, k) > maxlen:
                    maxlen = dp(i, k)
                    print(a, B[k])
                    print(A[i: i + maxlen], B[k: k + maxlen])

        return maxlen


from typing import List
from functools import lru_cache


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        maxlen = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    maxlen = max(dp[i][j], maxlen)
        return maxlen

#
# for j in range(0, -1, -1):
#     print("jaja")
#
# for j in range(0, -1, -1):
#     print("jaja")
