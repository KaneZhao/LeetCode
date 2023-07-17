"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater, stack = {}, []
        i = len(nums2) - 1
        while i >= 0:
            while len(stack) > 0 and nums2[i] >= stack[-1]:
                stack.pop()
            greater[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums2[i])
            i -= 1
        return [greater[i] for i in nums1]         