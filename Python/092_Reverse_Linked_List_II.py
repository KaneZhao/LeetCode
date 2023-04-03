"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = head
        for i in range(left - 1):
            pre = pre.next
        start = pre.next
        rev_node = None
        for i in range(right - left + 1):
            post = start.next
            start.next = rev_node
            rev_node = start
            start = post
        pre.next.next = start
        pre.next = rev_node 
        return dummy.next        