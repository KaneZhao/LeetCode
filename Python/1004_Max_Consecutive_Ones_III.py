"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""

"""
Using the sliding window, use a variable cnt to record the number of 0s that are currently changed to 1s. When traversing the array, if 0 is encountered, cnt will be incremented by 1. If cnt is greater than K at this time, it means that the window should be reduced. Use a while loop. If the left boundary is 0, after removing it, cnt should be decremented by 1 and left should be incremented by 1. Update the result res with the window size each time
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j, cnt, res = 0, 0, 0, 0
        while j < len(nums):
            if nums[j] == 0:
                cnt += 1
            while cnt > k:
                if nums[i] == 0:
                    cnt -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res            
                    

        