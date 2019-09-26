# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def post(n):
            if n == None:
                return 0, 0, 0 # cnt if inc, cnt if dec, regional max
            (li, ld, lm), (ri, rd, rm) = post(n.left), post(n.right)
            maxi, maxd,maxl = 1, 1, 1
            if n.left is not None:
                if n.val - n.left.val == 1: # inc
                    maxi = li + 1
                elif n.left.val - n.val == 1: # dec # the path is dec
                    maxd = ld + 1
                # maxl = max(maxi, maxd)
            if n.right is not None:
                if n.val - n.right.val == 1: # inc
                    maxl = max(maxl, maxd + ri)
                    maxi = max(maxi, ri + 1)
                elif n.right.val - n.val == 1: # dec # the path is dec
                    maxl = max(maxl, maxi + rd)
                    maxd = max(maxd, rd + 1)
            return maxi, maxd, max(lm, rm, maxl, maxi, maxd)
        return post(root)[2]

from lc297 import Codec

c = Codec()
r = c.deserialize("1,2,4,None,None,None,3")

def p(n):
    if n == None:
        print("None,")
        return
    p(n.left)
    p(n.right)
    print(n.val)
# p(r)

s = Solution()
ss = s.longestConsecutive(r)
print(ss)

cnt = {}
nums = [0] * 3
nums[1] = 2
print(nums)
# l = 0
# presum = [ 0 if i == 0 else nums[i] + presum[i - 1] for i in range(l + 1)]