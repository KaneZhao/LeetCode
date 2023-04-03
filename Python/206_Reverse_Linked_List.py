"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Using recursion to reverse a singly linked list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head):
            if head is None or head.next is None:
                return head
            node = helper(head.next)
            head.next.next = head   
            head.next = None
            return node
        return helper(head)    