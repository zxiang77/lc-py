from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # expanding both islands
        m, n = len(A), len(A[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isvalid(i, j):
            return 0 <= i < m and 0 <= j < n

        def island(i, j):
            return isvalid(i, j) and A[i][j] == 1

        def isbd(i, j):  # must be one
            if 0 == i or m - 1 == i or 0 == j or n - 1 == j:
                return True
            for dir in dirs:
                if A[i + dir[0]][j + dir[1]] == 0:
                    return True
            return False

        visited = [[False for i in range(n)] for j in range(m)]
        ls = [set() for i in range(2)]

        def find():
            nonlocal m, n
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1 and not visited[i][j]:
                        return (i, j)
            return (-1, -1)

        def getisland(x, y, ii):
            ls[ii].add((x, y))
            visited[x][y] = True
            q = deque()
            q.append((x, y))
            while len(q) > 0:
                l = len(q)
                for i in range(l):
                    cur = q.popleft()
                    for d in dirs:
                        nx, ny = cur[0] + d[0], cur[1] + d[1]
                        if isvalid(nx, ny) and A[nx][ny] == 1 and not visited[nx][ny]:
                            ls[ii].add((nx, ny))
                            q.append((nx, ny))
                            visited[nx][ny] = True

        x, y = find()
        # print("hh{}".format((x,y)))
        getisland(x, y, 0)
        x, y = find()
        # print("hh{}".format((x,y)))
        if x == -1:  # there is no the second island
            return -1
        getisland(x, y, 1)
        bs = [deque([j for j in i if isbd(j[0], j[1])]) for i in ls]  # boundaries

        dist = 0

        def exp(ii):
            nonlocal dist
            l = len(bs[ii])
            # nb = []
            for i in range(l):
                cur = bs[ii].popleft()
                for d in dirs:
                    nx, ny = (cur[0] + d[0], cur[1] + d[1])
                    if (nx, ny) in ls[1 - ii]:
                        return True
                    if isvalid(nx, ny) and (not visited[nx][ny]) and A[nx][ny] == 0:

                        visited[nx][ny] = True
                        A[nx][ny] = 1
                        ls[ii].add((nx, ny))
                        bs[ii].append((nx, ny))
                        # nb.append((nx, ny))
            # for (x, y) in nb:
            #     A[x][y] = True
            dist += 1
            return False

        e = 0
        while not exp(e):
            # print("tr")
            # [print(list(i)) for i in ls]
            # print(A)
            e = 1 - e
        return dist


# cases = []
# cases.append([[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]])
# for c in cases:
#     r = Solution().shortestBridge(c)
#     print(r)
f = list("fab")
f[0], f[1] = f[1], f[0]
print(f)