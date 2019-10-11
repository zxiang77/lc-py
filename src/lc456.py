from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # if inc, care if the third value is in the range,
        # if dec, only care if the previous value is less than both, so it's better search only dec pattern
        v = len(nums)
        if v < 3:
            return False

        minarr = [nums[0]]

        for i in range(1, len(nums)):
            minarr.append(min(minarr[-1], nums[i]))
            # min from [0, i - 1] i > 0
        stk = []
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > minarr[i]:
                while stk and stk[-1] <= minarr[i]:
                    stk.pop()
                if stk and nums[i] > stk[-1] > minarr[i]:
                    return True
                stk.append(nums[i])
        return False
