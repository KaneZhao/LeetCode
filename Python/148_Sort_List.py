"""
Given the head of a linked list, return the list after sorting it in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Using divide and conquer
    """
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Split the list into two halves using slow and fast pointers
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None 

        # Sort both halves recursively
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy

        # Merge the two lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append the remaining nodes
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next