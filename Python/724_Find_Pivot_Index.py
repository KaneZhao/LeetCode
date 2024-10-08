"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 1
        while len(nums) > 1 and i < len(nums):
            nums[i] += nums[i - 1]
            i += 1
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == nums[-1]:
                    return 0
            else:
                if nums[i - 1] == nums[-1] - nums[i]:
                    return i
        return -1                       