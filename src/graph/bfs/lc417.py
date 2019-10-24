from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # dijkstra -1, connected to neither, 1 connect to pac, 2 connect to atl, 3 connect to both, 0 UNK
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return [[]]
        stats = {}
        pac = []
        atl = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            pac.append((i, 0))
            atl.append((i, n - 1))

        for i in range(n):
            pac.append((0, i))
            atl.append((m - 1, i))

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def bfs(ocean, idx):
            visited = set(ocean)
            def valid(x, y):
                nonlocal m,n
                return 0 <= x < m and 0 <= y < n and (x, y) not in visited

            q = deque(visited)
            for o in visited:
                stats[o] = stats.get(o, 0) + idx
            while q:
                (px, py) = q.popleft()
                for (dx, dy) in dirs:
                    nx, ny = dx + px, dy + py
                    if valid(nx, ny) and matrix[nx][ny] >= matrix[px][py]:
                        newpos = (nx, ny)
                        q.append(newpos)
                        visited.add(newpos)
                        stats[newpos] = stats.get(newpos, 0) + idx
        bfs(pac, 1)
        bfs(atl, 2)

        res = []
        for i, v in stats.items():
            if v == 3:
                res.append(list(i))
        return res
