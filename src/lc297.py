# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = int(x)
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # make a full tree first
        self.res = []
        self.preorder(root)
        return ",".join(self.res)

    def preorder(self, root):
        if (root == None):
            self.res.append(str(None))
            return
        self.res.append(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)

    def dep(self, root):
        if root == None:
            return 0
        return max(self.dep(root.left), self.dep(root.right)) + 1

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        stack = []
        root = TreeNode(arr[0]) if arr[0] != "None" else None

        if root == None:
            return root
        l = True
        stack.append(root)  # node, left?

        for i in range(1, len(arr)):
            par = stack[-1]
            leaf = par.left == None and par.right == None
            if arr[i] == "None":
                if leaf:
                    if l:
                        l = False
                    else:
                        stack.pop()
                else:  # non leaf
                    # no worry parents are all non leaf
                    while par.right != None:  # right occupied. not yours
                        stack.pop()
                        par = stack[-1]
                    stack.pop()  # take up the right
                continue

            # add left when leaf, right when not
            # can't have invalid tree
            cur = TreeNode(arr[i])
            if leaf:
                if l:
                    par.left = cur
                else:
                    par.right = cur
            else:
                par.right = cur
            stack.append(cur)
            l = True
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))