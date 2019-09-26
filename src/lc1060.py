class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        ns, l = nums, len(nums)
        cnt = 0
        i, j = 0, l - 1
        gtcnt = lambda x: ns[x] - ns[0] - x
        while i < j:
            m = i + (j - i) // 2 #
            cnt = ns[m] - ns[0] - m
            if cnt > k: # want to get the one on the edge
                j = m
            else:
                i = m + 1
        # check if i goes over
        cnt = gtcnt(i)
        while cnt < k and i + 1 < l and gtcnt(i + 1) == cnt:
            i += 1
        while cnt >= k and i - 1 >= 0 and gtcnt(i - 1) == cnt:
            i -= 1
        return ns[i] - (cnt - k + 1) if cnt >= k else ns[i] + (k - cnt)
