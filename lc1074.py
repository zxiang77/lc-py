from typing import List
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        mt = matrix
        m, n = len(mt), len(mt[0])
        sums = [[0 for _ in range(n)] for _ in range(m)]
        total = 0
        def gt(i, j):
            if i < 0 or j < 0:
                return 0
            return sums[i][j]
        for i in range(m):
            rsum = 0
            mem = [dict() for wtf in range(i + 1)]
            for iiii in range(i + 1):
                mem[iiii][0] = 1
            for j in range(n):
                rsum += mt[i][j]
                sums[i][j] = rsum + gt(i - 1, j)

                for k in range(i + 1):

                    num = sums[i][j] - gt(k - 1, j)
                    l = num - target
                    total += mem[k].get(l, 0)

                    mem[k][num] = mem[k].get(num, 0) + 1


        return total


weights = [1,1,1]
tot, l = 0, len(weights)
        pres = [tot += weights[i] for i in range(l)]