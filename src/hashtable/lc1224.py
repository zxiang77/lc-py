from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        minv = 0
        cnt, d1ct = {}, {}

        def addcnt(v, cnt0):
            if cnt0 not in cnt.keys():
                cnt[cnt0] = set()
            cnt[cnt0].add(v)
            if cnt0 > 1:
                cnt[cnt0 - 1].remove(v)
                if len(cnt[cnt0 - 1]) == 0:
                    del cnt[cnt0 - 1]

        for i, n in enumerate(nums):
            d1ct[n] = d1ct.get(n, 0) + 1
            v = d1ct[n]
            addcnt(n, v)
            if len(d1ct) == 1:
                minv = i + 1

            if len(cnt) == 1:
                for k in cnt.keys():
                    if k == 1:
                        minv = i + 1

            if len(cnt) == 2:
                arr = []
                for k in cnt.keys():
                    arr.append(k)
                larger, smaller = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
                if (larger - smaller == 1 and len(cnt[larger]) == 1) or (smaller == 1 and len(cnt[smaller]) == 1 ): # count only differ by 1 and larger only has 1 element
                    minv = i + 1
        return minv
