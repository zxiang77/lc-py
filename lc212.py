from typing import List


class Node:
    def __init__(self, end): # char
        # self.c = c
        self.end = end
        self.children = [None for i in range(26)]

    def insert(self, st):
        if len(st) == 0:
            self.end = True
            return
        cur = self
        for i in range(len(st)):
            idx = ord(st[i]) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(st[i], False)
            cur = cur.children[idx]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # dfs + trie
        rt = Node('', False)
        for w in words:
            rt.insert(w)
        m, n = len(board), len(board[0])
        pos = lambda i, j: i * n + j
        c2i = lambda c: ord(c) - ord('a')
        i2c = lambda i: chr(i + ord('a'))
        ans = []
        ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def search(i, j, n, path, vst): #
            if n.end == True:
                ans.append("".join(path))
            for d in ds:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and pos(ni, nj) not in vst \
                    and n.children[c2i(board[ni][nj])] != None:
                    path.append(board[ni][nj])
                    vst.add(pos(ni, nj))
                    search(ni, nj, n.children[c2i(board[ni][nj])], path, vst)
                    vst.remove(pos(ni, nj))
                    del path[-1]

        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if rt.children[c2i(c)] != None:
                    search(i, j, [c], rt.children[c2i(c)], set([pos(i, j)]))

        return ans