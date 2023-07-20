"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = [0]
        for i in range(len(nums)):
            res.append(res[i] + nums[i])
        if target > res[-1]:
            return 0
        cnt, start = len(nums), 0
        for i in range(1, len(res)):
            while start <= i and res[i] - res[start] >= target:
                cnt = min(cnt, i - start) 
                start += 1
        return cnt
