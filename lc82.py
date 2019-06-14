# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if head is
        dummy = ListNode(-1)
        dummy.next = head
        self.helper(dummy)
        return dummy.next

    def helper(self, node):  # node is the previous cleaned node (none dupe)
        # if node is duplicate, then resolve it in this closure
        if node is None or node.next != None:
            return node
        nxt = node.next
        nnxt = nxt.next
        # nnnxt = None
        if nnxt is not None and nnxt.val is nxt.val:  # dupe
            while nnxt != None and nnxt.val == nxt.val:
                nnxt = nnxt.next
            nxt = nnxt  # remove dupe

        node.next = nxt
        helper(node.next)

