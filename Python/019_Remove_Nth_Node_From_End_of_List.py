"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre, p, q = ListNode(-1), head, head
        node, pre.next, node.next = pre, head, head
        while n - 1 > 0:
            q = q.next
            n -= 1
        while q!= None and q.next != None:
            p = p.next
            pre = pre.next
            q = q.next
        pre.next = p.next
        return node.next            