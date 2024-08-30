"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = nums.copy()
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = res[i]   