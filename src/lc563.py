# Definition for a binary tree node.

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        su = [0]

        def helper(n):
            if n == None:
                return 0, 0
            (ls, lt), (rs, rt) = helper(n.left), helper(n.right)
            su[0] += abs(lt - rt)
            return ls + rs + n.val, abs(lt - rt)

        _, t = helper(root)
        return su[0]

def gg(pos, dir):
    b = {}
    def hh():
        # nonlocal b
        b.keys()