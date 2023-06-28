"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(ls1, ls2):
            if ls1 is None:
                return ls2
            if ls2 is None:
                return ls1
            if ls1.val < ls2.val:
                ls1.next = helper(ls1.next, ls2)
                return ls1
            else:
                ls2.next = helper(ls1, ls2.next)
                return ls2
        return helper(list1, list2)            

            