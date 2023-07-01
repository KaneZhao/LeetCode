"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pleft, pright = ListNode(-1), ListNode(-1)
        tmpleft, tmpright = pleft, pright
        while head:
            if head.val < x:
                tmpleft.next = head
                tmpleft = tmpleft.next
            else:
                tmpright.next = head
                tmpright = tmpright.next
            head = head.next        
        tmpleft.next = pright.next
        tmpright.next = None
        return pleft.next            
