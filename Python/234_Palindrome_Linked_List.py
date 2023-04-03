"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

node: Put the linked list node into a stack, and then take it out, at this time the order of the elements is reversed
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    left = None
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global left
        left = head
        return self.reverse(head)

    def reverse(self, right):
        global left
        if right is None:
            return True
        last = self.reverse(right.next)
        last = last and (right.val == left.val)
        left = left.next
        return last        