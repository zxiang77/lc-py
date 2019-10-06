import heapq

class Solution:
    def racecar(self, target: int) -> int:
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, target = heapq.heappop(pq)
            if dist[target] > steps: # ??????????
                continue
            for k in range(K + 1):
                walk = (1 << k) - 1
                steps2, target2 = steps + k + 1, walk - target
                if walk == target: # destination
                    steps2 -= 1
                if abs(target2) < barrier and steps2 < dist[target2]:
                    heapq.heappush(pq, (steps2, target2))
                    dist[target2] = steps2
        return dist[0]
