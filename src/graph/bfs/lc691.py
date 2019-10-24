from collections import deque
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        vst = set()

        q, l = [], len(stickers)
        mps = []
        imp = {} # index mapping
        chars = [chr(i + ord('a')) for i in range(26)]

        def build(s, tar=-1):
            nonlocal l
            ret = {}
            for c in s:
                ret[c] = ret.get(c, 0) + 1
                if tar > 0:
                    if c not in imp.keys():
                        imp[c] = []
                    imp[c].append(tar)
            return ret

        for i, s in enumerate(stickers):
            mps.append(build(s, i))
        tars = build(target)

        # check if we have all the keys
        for i, j in enumerate(tars):
            if j > 0:
                if chr(i + ord('a')) not in imp.keys():
                    return -1

        def tostr(mp):
            s = ""
            for i, c in enumerate(chars):
                if mp.get(c, 0) > 0:
                    s += c + str(mp.get(c, 0))
            return s

        q = deque([(tars, 0)])
        vst.add(target)
        dep = 0
        while q:
            lq = len(q)
            for _ in range(lq):
                cur, idx = q.popleft()
                kset = set()
                dep += 1
                for kk in cur.keys(): # i can use
                    for ks in imp[kk]:
                        if ks >= idx:
                            kset.add(ks)
                for ks in kset: # potential to use
                    nm, m2 = {}, mps[ks]
                    for kk in cur.keys():
                        if cur[kk] - m2.get(kk, 0) > 0:
                            nm[kk] = cur[kk] - m2.get(kk, 0)
                    if len(nm.keys()) == 0:
                        return dep
                    nmstr = tostr(nm)
                    if nmstr not in vst:
                        vst.add(nmstr)
                        q.append((nm, ks))
        return -1
