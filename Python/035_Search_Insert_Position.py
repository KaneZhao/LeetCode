"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         # Define target in the range of left-closed and right-closed, [left, right]
        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1 # target is in the left interval, so [left, middle - 1]
            elif nums[mid] < target:
                left = mid + 1 # target is in the right interval, so [middle + 1, right]         
        return left    