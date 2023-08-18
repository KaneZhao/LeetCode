"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = head
        pre = node
        while pre.next:
            if pre.next.next:
                cur = pre.next
                pre.next = cur.next
                cur.next = pre.next.next
                pre.next.next = cur
                pre = cur
            else:
                break    
        return node.next        