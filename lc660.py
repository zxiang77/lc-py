class Solution:
    def newInteger(self, n: int) -> int:
        # counting
        if n < 9:
            return n
        if n == 9:
            return 8
        k, l = n, []
        while k > 0:
            l.append(k % 10)
            k /= 10
        l = l[::-1]
        ctr = [0 for i in range(len(l) + 1)]
        ctr[-1] = 1
        ctr[-2] = 8

        for i in range(len(ctr) - 2, 0, -1): # make sure first i larger than 0
            ctr[i] = ctr[i + 1] * 8

        for i in range(len(l)): # for # less than prefix
            if l[i] != 0:
                ctr[0] += (l[i] - 1) * ctr[i + 1]
            if l[i] == 9:
                break
        return sum(ctr)
            

        # add all #