from collections import deque
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        dirs = [('d', (1, 0)), ('l', (0, -1)), ('r', (0, 1)), ('u', (-1, 0))]
        # bt
        visited = set()
        # bt with bfs
        q = deque([(None, ball, "")])
        m, n = len(maze), len(maze[0])

        def valid(x, y):
            nonlocal m, n
            return 0 <= x < m and n > y >= 0 and maze[x][y] == 0

        while len(q) > 0:
            l = len(q)
            for _ in range(l):
                (prev, cur, cch) = q.popleft()
                for ch, d in dirs:
                    x, y = cur[0], cur[1]
                    while valid(x + d[0], y + d[1]):
                        x += d[0]
                        y += d[1]

                        if x == hole[0] and y == hole[1]:
                            # end here
                            res = ch + cch
                            # print("ch: " + ch)
                            while prev != None:
                                print(prev)
                                (prev, _, cch) = prev
                                res += cch
                            return res[::-1]


                    dup = False
                    prevrf, currf = prev, cur
                    while prevrf != None:
                        if currf[0] == x and currf[1] == y:
                            dup = True
                            break
                        (prevrf, currf, _) = prevrf

                    if not dup:
                        # print(x, y)
                        q.append(((prev, cur, cch), (x, y), ch))

        return 'impossible'

r = Solution().findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1])
print(r)
