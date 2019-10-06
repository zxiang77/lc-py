class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # find kite, then fnd k*t*, it could be any from the k*t*, but with the closest distance
        # 3 indexes, 1 exact word (set),
        vows = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s3t, casediff, vowdiff = set(), {}, {}

        def tokey(s):
            k = ""
            s = s.lower()
            for c in s:
                k += "*" if c in vows else c
            return k

        for w in wordlist:
            s3t.add(w)
            lo = w.lower()
            if lo not in casediff.keys():
                casediff[lo] = w

            k = tokey(w)
            if k not in vowdiff.keys():
                vowdiff[k] = w

        res = []
        for q in queries:
            lo = q.lower()
            k = tokey(q)
            if q in s3t:
                res.append(q)
            elif lo in casediff.keys():
                res.append(casediff[lo])
            elif k in vowdiff.keys():
                res.append(casediff.get(vowdiff[k].lower(), vowdiff[k]))
            else:
                res.append("")
        return res

    def insert(self, d1ct, lo, w):
        if lo in d1ct.keys():
            return
        d1ct[lo] = w

