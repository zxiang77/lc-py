from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = [[1, 2, 3], [4, 5, 0]]
        w = [[6 ** 0, 6 ** 1, 6 ** 2], [6 ** 3, 6 ** 4, 6 ** 5]]
        def t2n(ar):
            tot = 0
            for i in range(2):
                for j in range(3):
                    tot += ar[i][j] * w[i][j]
            return tot

        def n2t(n):
            ar = []
            for i in range(5, -1, -1):
                r, c = i // 3, i % 3
                ar.append(n // w[r][c])
                n = n % w[r][c]
            ar.reverse()
            return [ar[:3], ar[3:]]
        
        q = deque([(t2n(start), (1, 2))])
        vst = set()
        vst.add(t2n(start))
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cnt = 0
        dest = t2n(board)
        while q:
            l = len(q)
            cnt += 1
            for _ in range(l):
                cur, pos = q.popleft()
                cur = n2t(cur)
                for d in ds:
                    ni, nj = pos[0] + d[0], pos[1] + d[1]
                    if 0 <= ni < 2 and 0 <= nj < 3:
                        cur[ni][nj], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[ni][nj]
                        n = t2n(cur)
                        if n == dest:
                            return cnt
                        if n not in vst:
                            vst.add(n)
                            q.append((n, (ni, nj)))
                
        
        return -1