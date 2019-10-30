import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        pq = []  # max size of k
        cpmap = []
        for i in range(len(Profits)):
            heapq.heappush(cpmap, (Capital[i], Profits[i]))

        total, prj = W, k
        while cpmap:
            c, p = heapq.heappop(cpmap)
            if c > total:  # this condition is unnecessary
                if not pq or prj == 0:
                    return total
                p2, c2 = heapq.heappop(pq)
                if c2 > total:
                    return total
                total -= p2
                prj -= 1
            heapq.heappush(pq, (-p, c))

        while prj > 0 and pq:
            # could be an unreacheable for current total there could be cases when you don't want to pursue high
            # capital projects, but to stay with low cap, high prof project
            p, c = heapq.heappop(pq)
            total -= p
            prj -= 1
        return total
cases = [(2, 0, [1,2,3], [0,1,1]), (3, 0, [1,2,3], [0,1,2])]


s = Solution()
for p1, p2, p3, p4 in cases:
    print(s.findMaximizedCapital(p1, p2, p3, p4))