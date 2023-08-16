"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Set a virtual head node to perform the delete operation
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = head
        pre, cur = node, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return node.next                