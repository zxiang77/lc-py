from typing import List


class Solution:
    def __init__(self):
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        lookup = {}
        # or could possibly sort the list first
        for n in nums:
            lookup[n] = lookup.get(n, 0) + 1

        tmp = []
        for k, v in lookup.items():
            tmp.append((k, v))
        runner = []
        res = []
        self.helper(tmp, 0, runner, res)
        return res

    def helper(self, lookup, idx, runner, res):
        if idx == len(lookup):
            return

        ctr = lookup[idx][1]
        for x in range(ctr):
            runner.append(lookup[idx][0])
            res.append(runner.copy())
            self.helper(lookup, idx + 1, runner, res)

        for x in range(ctr):
            del runner[-1]
