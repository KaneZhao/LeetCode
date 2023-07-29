"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""
# for 0 <= nums1[i], nums2[i] <= 1000, we build a list to obtian all elements
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = [0] * 1001
        for i in nums1:
            lst[i] = 1
        for j in nums2:
            if lst[j] == 1:
                lst[j] = 2
        return [k for k, v in enumerate(lst) if v == 2]        