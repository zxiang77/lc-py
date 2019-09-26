# Definition for a binary tree node.
class w:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.id = 0


class Solution:

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # how to find id of a tree?
        # sub problem, find all tree type of all subtrees
        # left id + right id + cur => new id
        ids = {}
        dups = []

        def id(i, j, k): # wut hasher?
            return "({}-{}--{})".format(k, i, j)

        def postorder(root):
            if root == None:
                return None
            l, r = postorder(root.left), postorder(root.right)
            # do what
            nid = id(l.id if l != None else '#', r.id if r != None else '#', root.val)
            cur = w(root)
            cur.left, cur.right, cur.id = l, r, nid
            if nid not in ids.keys():
                ids[nid] = 0
            # dup, added = False, False
            ids[nid] += 1
            if ids[nid] == 2:
                dups.append(root)
            return cur

        postorder(root)
        return dups
