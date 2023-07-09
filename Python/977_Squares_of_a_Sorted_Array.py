"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                res.append(nums[right] * nums[right])
                right -= 1
            else:
                res.append(nums[left] * nums[left])
                left += 1                                   
        return res[::-1]            
