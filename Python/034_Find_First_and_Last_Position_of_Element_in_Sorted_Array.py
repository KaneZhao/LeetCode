"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while i >= 0 and nums[i] == target:
                    res[0] = i
                    i -= 1
                while j <= len(nums) - 1 and nums[j] == target:
                    res[1] = j 
                    j += 1   
                return res    
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res                 
