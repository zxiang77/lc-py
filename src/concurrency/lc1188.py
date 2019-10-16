import threading
from collections import deque


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.cap = capacity
        self.store = deque()
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        self.cond.acquire()
        while len(self.store) == self.cap:
            self.cond.wait()
        self.store.append(element)
        self.cond.notify()
        self.cond.release()

    def dequeue(self) -> int:
        self.cond.acquire()
        while len(self.store) == 0:
            self.cond.wait()
        v = self.store.popleft()
        self.cond.notify()
        self.cond.release()
        return v

    def size(self) -> int:
        return len(self.store)
