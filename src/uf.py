class uf:
    def __init__(self, m, n):
        self.m, self.n = m, n
        nn = m * n
        self.ids = [i for i in range(nn)]
        self.szs = [1 for i in range(nn)]

    def union(self, i, j):
        iid, jid = self.find(i), self.find(j)
        id1, id2 = (iid, jid) if self.szs[iid] > self.szs[jid] else (jid, iid)
        self.szs[id1] += self.szs[id2]
        self.ids[id2] = self.ids[id1]

    def find(self, k):
        if self.ids[k] != k:
            return self.find(self.id[k])
        return self.ids[k]

    def uid(self, i, j):
        return i * self.n + j
