"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p_a, p_b = headA, headB
        len_a, len_b = 0, 0
        while p_a.next != None:
            len_a += 1
            p_a = p_a.next

        while p_b.next != None:
            len_b += 1
            p_b = p_b.next

        if p_a != p_b:
            return None
        else:
            t_a, t_b = headA, headB
            if len_a >= len_b:
                while len_a > len_b:
                    t_a = t_a.next
                    len_b += 1
            else:
                while len_b > len_a:
                    t_b = t_b.next
                    len_a += 1
            while t_a != t_b:
                t_a = t_a.next
                t_b = t_b.next
            return t_a            


