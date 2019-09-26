class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = len(nums)
        i, j = 0, 1000000

        while i <= j:
            m = i + (j - i) // 2 # find the
            sumk = 0
            for ii in range(l - 1): # n log n log D
                bi, bj = ii, l - 1
                inc = False
                while bi <= bj: # bsearch with duplicate
                    bm = bi + (bj - bi) // 2
                    d = nums[bm] - nums[ii]
                    if d > m:
                        bj = bm - 1
                    elif d < m:
                        bi = bm + 1
                    else: # check if it's the right most
                        if bm == l - 1 or nums[bm + 1] - nums[ii] > m:
                            inc = True
                            bi = bm
                            break
                        else:
                            bi = bm + 1
                sumk += min(bi, bj) - ii

            if sumk > k: # bsearch that k in a range, need to find the largest sumk < k
                j = m - 1 # need to find the lowest number larger than k
            elif sumk < k:
                # for num i, if i is the right number, then sumk for i lb <= k <= rb
                i = m + 1
            else:
                if inc:
                    return m
                j = m - 1
        return i
