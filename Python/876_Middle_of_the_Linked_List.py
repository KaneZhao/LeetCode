"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p, q = head, head
        node_len = 0
        while p:
            node_len += 1
            p = p.next
        mid_len = node_len // 2   
        while mid_len > 0:
            q = q.next
            mid_len -= 1
        return q   
