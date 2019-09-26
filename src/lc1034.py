from collections import deque
from typing import List

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = [[False for j in range(self.n)] for i in range(self.m)]
        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.borderline = []

        q = deque([])
        q.append((r0, c0))
        v = grid[r0][c0]
        while len(q) > 0:
            cur = q.popleft()
            if self.isborder(cur[0], cur[1], v):
                self.borderline.append(cur)
            self.visited[cur[0]][cur[1]] = True
            for d in self.dirs:
                ni, nj = cur[0] + d[0], cur[1] + d[1]
                if self.isvalid(ni, nj, v):
                    q.append((ni, nj))

        for b in self.borderline:
            grid[b[0]][b[1]] = color
        return grid

    def isvalid(self, i, j, v):
        return i >= 0 and i < self.m and j >= 0 and j < self.n and not self.visited[i][j] and self.grid[i][j] == v

    def isborder(self, i, j, v):  # check if
        if i == 0 or i == self.m - 1 or j == 0 or j == self.n - 1:
            return True

        for [x, y] in self.dirs:
            if self.grid[i + x][j + j] != v:
                return True
        return False

    min