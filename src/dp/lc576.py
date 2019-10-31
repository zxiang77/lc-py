class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def getres(i):
            return i % (1e9 + 7)
        total = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[i][j] = 1
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q = set([(i, j)])
        stp = 0
        def valid(x, y):
            nonlocal m, n
            return 0 <= x < m and 0 <= y < n
        while q:
            if stp == N:
                break
            newdp = [[0 for _ in range(n)] for _ in range(m)]
            newq = set()
            for cx, cy in q:
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if valid(nx, ny):
                        newdp[nx][ny] += dp[cx][cy]
                        newq.add((nx, ny)) # for all cells that is reached with k steps, but it could be multiple times
                    else:  # off bound
                        total += dp[cx][cy]
            dp = newdp
            q = newq
            stp += 1
        return getres(total)

# takeaway: this should use set for next iteration instead of deque, because we are allowing duplicate move to the same cell