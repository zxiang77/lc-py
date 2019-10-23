import heapq
from collections import deque
from typing import List

# solution: heap + bfs todo:z
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        dirs = [('d', (1, 0)), ('l', (0, -1)), ('r', (0, 1)), ('u', (-1, 0))]
        # bt
        visited = {}
        # bt with bfs
        visited[(ball[0], ball[1])] = (0, "")
        q = [(0, (ball[0], ball[1]), '')]
        m, n = len(maze), len(maze[0])
        hole = tuple(hole)

        def valid(x, y):
            nonlocal m, n
            return 0 <= x < m and 0 <= y < n and maze[x][y] != 1

        def strcmp(s1, s2):
            l = min(len(s1), len(s2))
            for i in range(l):
                if ord(s1[i]) > ord(s2[i]):
                    return 1
                elif ord(s1[i]) < ord(s2[i]):
                    return -1
            return len(s1) - len(s2)

        while q:
            stps, pos, str = heapq.heappop(q)

            if stps > visited.get(hole, (float('inf'), ''))[0]:
                break

            for dir, (dx, dy) in dirs:
                cx, cy = pos[0], pos[1] # current x, y
                dist = 0
                newstr = str + dir
                while valid(cx + dx, cy + dy):
                    cx += dx
                    cy += dy
                    dist += 1
                    if (cx, cy) == hole:
                        break

                current = (cx, cy)
                newstps = dist + stps
                newres = (newstps, newstr)
                if newres < visited.get(current, (float('inf'), "")):
                    visited[current] = newres
                    heapq.heappush(q, (newstps, current, newstr))
        return visited.get(hole, (0, 'impossible'))[1]

# r = Solution().findShortestWay([[0,1,0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0,0,1],[0,0,0,0,0,0,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[1,0,0,1,0,0,0,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,1,0]],[2,4],[7,6])
# print(r)
