from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        tailsum = [0 for _ in range(l)]

        tailsum[l - 1] = piles[l - 1]
        for i in range(l - 2, -1, -1):
            tailsum[i] = tailsum[i + 1] + piles[i]

        @lru_cache(None)
        def maxreturn(m, start):
            nonlocal l
            maxtake = 2 * m
            psum = 0
            maxret, maxoppo = 0, 0
            for i in range(maxtake):
                if start + i >= l:
                    break
                psum += piles[start + i]
                first, second = maxreturn(max(i + 1, m), start + i + 1)
                if psum + second > maxret:
                    maxret, maxoppo = psum + second, first

            return maxret, maxoppo

        alex, lee = maxreturn(1, 0)
        return alex