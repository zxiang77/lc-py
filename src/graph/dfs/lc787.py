import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dep = K + 1

        m4p = {}
        for (f, t, co) in flights:
            if f not in m4p.keys():
                m4p[f] = []
            m4p[f].append((t, co))

        shortest = [[float('inf') for _ in range(dep + 1)] for _ in range(n)]
        shortest[src] = [0 for _ in range(n)]

        q = [(0, 0, src)]

        while q:
            ncost, ndep, node = heapq.heappop(q)
            if ndep > dep or ncost > shortest[node][ndep]:
                continue
            if node == dst:
                return ncost

            for nxt, nxtco in m4p.get(node, []):
                if shortest[nxt][ndep + 1] > ncost + nxtco:
                    shortest[nxt][ndep + 1] = ncost + nxtco
                    heapq.heappush(q, (ncost + nxtco, ndep + 1, nxt))
        return -1
