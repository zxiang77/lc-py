from copy import deepcopy
from functools import lru_cache
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def ext(s1, s2):
            l1, l2 = len(s1), len(s2)
            kkk, le = 0, float('inf')
            for k in range(min(l1, l2)):
                if s1[len(s1) - k:] == s2[0 : k]:
                    nc = l1 + l2 - k
                    if nc < le:
                        kkk = k
                        le = nc
            return kkk # means save first one k chars

        l = len(A)
        g = [[0 for _ in range(l)] for _ in range(l)]

        for i in range(l):
            for j in range(i + 1, l):
                g[i][j] = ext(A[i], A[j])
                g[j][i] = ext(A[j], A[i])

        rs, ct = "", -1
        vs = 2 ** l - 1
        path = []
        ks = {}
        su = 0
        for i in range(l):
            ks[2 ** i] = i
            su += 2 ** i

        @lru_cache(None)
        def dp(i, hd): # is means state, hd means head
            nonlocal l, ks, g
            if i - (1 << hd) in ks.keys(): # i is the last node to visit
                gv = g[hd][ks[i - (1 << hd)]] # (what's next and how many saved by going this way)
                return [None, [ks[i - hd], gv]]
            i2 = i - (1 << hd)
            le, prev, idx = -1, [], 0
            for j in range(l):
                d = 1 << j
                if i2 & d > 0:
                    (prv2, cur) = dp(i2, j)
                    if le < cur[1] + g[hd][j]:
                        le = cur[1] + g[hd][j]
                        prev = [prv2, cur]
                        idx = j
            return [prev, [idx, le]]


        r = ""
        # print(path)
        maxl, st = 0, []
        for i in range(l):
            cur = dp(su, i)
            if cur[1][1] > maxl:
                maxl = cur[1][1]
                st = [cur, [i, 0]]

        (prev, cur) = st
        while cur != None:
            # (prev, cur) = s
            r += A[cur[0]] if prev == None else A[cur[0]][:len(A[cur[0]]) - prev[1][1]]

            if prev == None:
                break
            (prev, cur) = prev

        return r

"ttccatgcatc"
"gctaagttcatgcatc"
