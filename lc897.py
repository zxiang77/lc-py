
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def reorder(n):
            if n == None:
                return None, None
            if n.left == None and n.right == None:
                return n, n

            ll, lr = reorder(n.left)
            n.left = None
            if ll != None:
                lr.right = n

            rl, rr = reorder(n.right)
            lr.right = rl

            return (ll if ll != None else n), (rr if rr != None else n)
        return reorder(root)[0]

m, n = 1, 1
f = lambda x, y: x * n + y
