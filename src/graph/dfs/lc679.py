from typing import List

# this solution is wrong, need to be changed

class Frac:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def eval(self):
        return self.a / self.b

    def add(self, other):
        if isinstance(other, Frac):
            return Frac(self.a * other.b + other.a * self.b, self.b * self.a)
        return Frac(self.a + self.b * other, self.b)

    def sub(self, other):
        self.add(-other)

    def mult(self, ot):
        if isinstance(ot, Frac):
            return Frac(self.a * ot.a, self.b * ot.b)
        return Frac(self.a * ot, self.b)

    def div(self, ot):
        if isinstance(ot, Frac):
            return Frac(self.a * ot.b, self.b * ot.a)
        return Frac(self.a, self.b * ot)

    def __neg__(self):
        return Frac(-self.a, self.b)


def add(a, b):
    if not isinstance(a, Frac) and not isinstance(b, Frac):
        return a + b
    c, d = (a, b) if isinstance(a, Frac) else (b, a)
    return c.add(b)

def mult(a, b):
    if not isinstance(a, Frac) and not isinstance(b, Frac):
        return a * b
    c, d = (a, b) if isinstance(a, Frac) else (b, a)
    return c.mult(b)


def div(a, b):
    if not isinstance(a, Frac) and not isinstance(b, Frac):
        return a / b
    if isinstance(a, Frac):
        return a.div(b)
    else:
        return Frac(a * b.b, b.a) if isinstance(b, Frac) else Frac(a, b)
# ctr = 0
# nonlocal ctr
class Solution:
    @staticmethod
    def merger(arr, i, j):
        # get a l - 1 sized array, merging i-th and j-th value.
        # so the new value stays in i-th of the new array
        arrc = []
        arrc.extend(arr[0: i])
        arrc.append(0)
        arrc.extend(arr[j + 1:])
        arrc.copy()
        arrc[i] = arr[i].add(arr[j])
        yield arrc

        arrc = arrc.copy()
        arrc[i] = arr[i].div(arr[j])
        yield arrc

        arrc = arrc.copy()
        arrc[i] = arr[i].mult(arr[j])
        yield arrc

        if arr[j].eval() != 0:
            arrc = arrc.copy()
            arrc[i] = arr[i].div(arr[j])
            yield arrc

    def __init__(self):
        self.arr = []
        self.ctr = 0

    @staticmethod
    def enum(n):
        if not n:
            yield n
            return
        l = len(n)
        for i in range(l): # ith is the first one
            rest = []
            rest.extend(n[0 : i])
            rest.extend(n[i + 1 : ])
            for e in Solution.enum(rest):
                ret = [n[i]]
                ret.extend(e)
                yield ret


    def judgePoint24(self, nums: List[int]) -> bool:
        n2 = []
        for i in nums:
            n2.append(Frac(i, 1))
        for e in Solution.enum(n2):
            if self.helper(e):
                return True
        return False

        # compute two and try neighbors
        # fraction should be

    def helper(self, nums):
        if len(nums) == 1:
            # if (isinstance(nums[0], Frac) and abs(nums[0].eval() - 24) < 0.000000001) or abs(nums[0] - 24) < 0.0000001:
            if nums[0].b != 0 and nums[0].eval() == 24:
                return True
        l = len(nums)
        for i in range(l - 1):
            for sub in Solution.merger(nums, i, i + 1):
                if self.helper(sub):
                    return True
        return False
