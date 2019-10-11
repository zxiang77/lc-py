from typing import List
import random

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.map = {}
        self.rd = random.Random()
        l = len(blacklist)
        self.ceil = N - l
        for i in blacklist:
            if i >= self.ceil:
                self.map[i] = i # won't be reached
        tail = N - 1
        for i in blacklist:
            if i < self.ceil:
                while tail in self.map.keys():
                    tail -= 1
                self.map[i] = tail
                tail -= 1

    def pick(self) -> int:
        nxt = self.rd.randint(0, self.ceil - 1)
        return self.map.get(nxt, nxt)
