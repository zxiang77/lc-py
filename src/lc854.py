from collections import deque
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0
        mp = {} # shortest path to str
        a, n = list(A), len(A)

        visited = [set(), set()]
        qs = [deque([]), deque([])]
        qs[0].append(A)
        qs[1].append(B)
        visited[0].add(A)
        visited[1].add(B)
        dep, found = 0, False
        def bfs(ii):
            nonlocal dep, found
            # while len(qs[ii]) > 0:
            l = len(qs[ii])
            if l == 0:
                return True

            for _ in range(l):
                c = qs[ii].popleft()
                for i in range(n):
                    for j in range(i + 1, n):
                        if c[j] == c[i]:
                            continue
                        cl = list(c)

                        cl[i], cl[j] = cl[j], cl[i]
                        cl = "".join(cl)
                        print((ii, cl))
                        if cl in visited[1 - ii]:
                            found = True
                            return True
                        if cl in visited[ii]:
                            continue
                        qs[ii].append(cl)
                        visited[ii].add(cl)
            dep += 1
            return False

        ii = 0
        while not bfs(ii):
            ii = 1 - ii
        return dep if found else -1

p = [1, 2 , 3]
print(type(min(p)))
l = 2
visited = 0
for i in range(l):
    visited += 1 << i
print(visited)