"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height) -> int:
        if len(height) == 1:
            return 0
        res = height[:]
        left, right = height[:], height[:]
        lmax, rmax, hlen = 0, 0, len(height) 
        for i in range(1, hlen - 1):
            left[i] = max(left[i], left[i - 1])
            right[hlen - i - 1] = max(right[hlen - i - 1], right[hlen - i])
        print(left, right)    
        for i in range(1, hlen - 1):    
            if left[i - 1] == 0 or right[i + 1] == 0:
                res[i] = 0
            else:
                res[i] = max(min(left[i - 1], right[i + 1]) - res[i] ,0)
        return sum(res) - res[0] - res[-1]  