"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p, q = head, head.next
        while q:
            while p and q and p.val == q.val:
                q = q.next
            p.next = q
            p = p.next
            if q:
                q = q.next    
        return head        
