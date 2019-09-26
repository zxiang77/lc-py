class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        #
        dq = Deque()
        for i in range(len(deck) - 1, -1, -1):
            if dq.sz > 0:
                tmp = dq.rmtail()
                dq.addhead(tmp)
            dq.addhead(Node(deck[i]))
        res = []
        cur = dq.head
        while cur != None:
            res.append(cur.v)
            cur = cur.next
        return res


class Node:
    def __init__(self, v):
        self.prev = None
        self.next = None
        self.v = v


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0

    def rmhead(self):
        tmp = self.tail
        self.sz -= 1
        if self.sz == 0:
            self.head, self.tail = None, None
            return tmp
        self.head = self.head.next
        self.head.prev = None
        return tmp

    def rmtail(self):
        tmp = self.tail
        self.sz -= 1
        if self.sz == 0:
            self.head, self.tail = None, None
            return tmp

        self.tail = self.tail.next
        self.tail.next = None
        return tmp

    def addhead(self, n):
        self.sz += 1
        if self.head == None:
            self.head, self.tail = n, n
            return

        self.head.prev = n
        n.next = self.head
        self.head = n

    def addtail(self, n):
        self.sz += 1
        self.tail.next = n
        n.prev = self.tail
        self.tail = n