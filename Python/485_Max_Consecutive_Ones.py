"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

# This question is about finding the maximum number of consecutive 1s. 
# It is not a difficult problem. You can traverse the array and use a counter cnt to count the number of 1s. If the current number is 0, then cnt is reset to 0. If it is not 0, cnt is incremented by 1, and then the result res is updated each time.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, cur = 0, 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        return max(res, cur)            