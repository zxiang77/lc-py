from random import Random
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        total = 0

        # a = [(i, i) for i in arr]

        def reduce(a):
            nonlocal total
            l = len(a)
            if l == 1:
                return
            minprod = float('inf')
            for i in range(l - 1):
                minprod = min(minprod, a[i] * a[i + 1])
            nxt = []

            i = 0
            added = False
            while i < l:
                if i < l - 1 and minprod == a[i] * a[i + 1] and not added:
                    added = True
                    s0m = a[i] * a[i + 1]
                    total += s0m
                    nxt.append(max(a[1 + i], a[i]))
                    i += 2
                    continue
                nxt.append(a[i])
                i += 1
            reduce(nxt)

        reduce(arr)
        return total
#
# cases = [([6,2,4])]
# s = Solution()
# for p1 in cases:
#     print(s.mctFromLeafValues(p1))
# Random.randint(1, 15)
# print([(Random()).randint(1, 15) for i in range(40)])