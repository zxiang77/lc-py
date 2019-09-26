from typing import List
class Solution:
    class Node:
        def __init__(self, c):
            self.c = c
            self.children = set()

    class Rel:
        def __init__(self, fr, to):
            self.fr = fr
            self.to = to

    def alienOrder(self, words: List[str]) -> str:
        self.rels = set()
        self.chars = set()

        for w in words:
            for c in w:
                self.chars.add(c)

        l = len(words)
        self.nodes = {}
        self.rc = {}

        for c in self.chars:
            self.rc[c] = 0
            self.nodes[c] = Solution.Node(c)

        for i in range(l):
            for j in range(i + 1, l):
                r = self.cmp(words[i], words[j])
                if r != None:
                    if self.nodes[r.to] not in self.nodes[r.fr].children:
                        self.rc[r.to] += 1
                    self.nodes[r.fr].children.add(self.nodes[r.to])

        self.path = ""
        self.dfs()

        # if len(res) != len(self.chars):
        #     return res
        return self.path if self.path != None else ""

    def dfs(self):
        if self.path == None:
            return
        if 0 == len(self.chars):
            return self.path
        zeros = []
        for c in self.chars:
            if self.rc[c] == 0:
                zeros.append(c)

        if len(zeros) == 0: # if there is a loop
            self.path = None
            return

        togo = set()

        for z in zeros:
            self.path += z
            self.chars.remove(z)
            for n in self.nodes.get(z).children:
                self.rc[n.c] -= 1
                togo.add(n)
            del self.nodes[z]
        self.dfs()

    def cmp(self, a, b):  # a < b
        l = min(len(a), len(b))
        for i in range(l):
            ca, cb = a[i], b[i]
            if ca != cb:
                return Solution.Rel(ca, cb)
        return None

for i in range(10, 0, -1):
    print(i)