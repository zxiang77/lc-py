# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        n, voy = root, voyage
        # def tvs(n, voy):
        if n == None:
            return [] if len(voy) == 0 else [-1]

        if n.left == None and n.right == None:
            return [] if len(voy) == 1 and voy[0] == n.val else [-1]

        res = []
        if len(voy) < 2:
            return [-1]

        if n.val != voy[0]:
            return [-1]

        if n.left == None or n.right == None:
            return self.flipMatchVoyage(n.left, voy[1:]) if n.left != None else self.flipMatchVoyage(n.right, voy[1:])

        l, r = n.left.val, n.right.val
        li, ri = -1, -1
        for i in range(1, len(voy)):
            if voy[i] == l:
                li = i
            if voy[i] == r:
                ri = i
        if li == -1 or ri == -1:
            return [-1]

        rl, rr = [], []
        if ri < li:
            res.append(n.val)
            rl = self.flipMatchVoyage(n.left, voy[li:])
            rr = self.flipMatchVoyage(n.right, voy[1:li])
        else:
            rl = self.flipMatchVoyage(n.left, voy[1:ri])
            rr = self.flipMatchVoyage(n.right, voy[ri:])

        if (len(rl) > 0 and rl[0] == -1) or (len(rl) > 0 and rl[0] == -1):
            return [-1]

        for ele in rl:
            res.append(ele)

        for ele in rr:
            res.append(ele)

        return res

