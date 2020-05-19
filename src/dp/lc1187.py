import bisect
import collections
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        d1ct = {-1: 0}
        # after making the current index value increasing and end with k, v swaps are needed
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for k, v in d1ct.items():
                if k < i:
                    # safely reuse it
                    tmp[i] = min(v, tmp[i])
                nxt = bisect.bisect_right(arr2, k)
                if nxt < len(arr2):
                    nxt = arr2[nxt]
                    tmp[nxt] = min(1 + d1ct[k], tmp[nxt])
            d1ct = tmp
        return min(d1ct.values()) if d1ct else -1