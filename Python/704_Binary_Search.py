"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Define target in the range of left-closed and right-closed, [left, right]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1 # target is in the left interval, so [left, middle - 1]
            elif nums[mid] == target:
                return mid
            else:
                left = mid + 1 # target is in the right interval, so [middle + 1, right]
        # target value not found
        return -1                 