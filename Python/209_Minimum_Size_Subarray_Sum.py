"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cnt, sums, left = len(nums) + 1, 0, 0
        for i in range(len(nums)):
            sums += nums[i]
            while left <= i and sums >= target:
                cnt = min(cnt, i - left + 1)
                sums -= nums[left]
                left += 1
        return 0 if cnt == len(nums) + 1 else cnt   
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         res = [0]
#         for i in range(len(nums)):
#             res.append(res[i] + nums[i])
#         if target > res[-1]:
#             return 0
#         cnt, start = len(nums), 0
#         for i in range(1, len(res)):
#             while start <= i and res[i] - res[start] >= target:
#                 cnt = min(cnt, i - start) 
#                 start += 1
#         return cnt
    
# def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         i, res, min_len = 0, 0, 0
#         for j in range(len(nums)):
#             res += nums[j]
#             while res >= target:
#                 min_len = min(j - i + 1, min_len) if min_len > 0 else j - i + 1
#                 res -= nums[i]
#                 i += 1
#         return min_len          
