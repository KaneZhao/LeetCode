"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = nums[:], nums[:]
        for i in range(1, len(nums)):
            left[i] *= left[i - 1]
            right[len(nums) - i - 1] *= right[len(nums) - i]
        for i in range(len(nums)):
            if i == 0:
                nums[i] = right[1]
            elif i == len(nums) - 1:
                nums[i] = left[-2]
            else:
                nums[i] = left[i - 1] * right[i + 1]
        return nums                    