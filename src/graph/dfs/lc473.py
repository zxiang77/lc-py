from typing import List

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False

        su = sum(nums)
        if su % 4 != 0:
            return False
        side = su / 4
        nums.sort()
        used = [False for _ in nums]
        # if counstructing the same edge, only look from later
        def dfs(total, start):
            if total == su:
                return True

            target = ((total // side) + 1) * side
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if total + nums[i] > target:
                    break
                used[i] = True
                if total + nums[i] == target and dfs(total + nums[i], 0):
                    return True
                elif total + nums[i] < target and dfs(total + nums[i], i + 1):
                    return True
                used[i] = False
            return False
        return dfs(0, 0)
