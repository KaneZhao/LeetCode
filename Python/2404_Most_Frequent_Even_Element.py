"""
Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.
"""
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i % 2 == 0:
                dic[i] = dic.get(i, 0) + 1
        if len(dic) <= 0:
            return -1        
        res, cnt = 100000, 0
        for k, v in dic.items():
            if v > cnt:
                res, cnt = k, v
            elif v == cnt:
                res = min(res, k)    
        return res                