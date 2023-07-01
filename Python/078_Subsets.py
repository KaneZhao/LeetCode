"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        res = []    
        cur = nums[-1]    
        nums.pop()
        tmp = self.subsets(nums)
        for i in tmp:
            j = i[:]
            j.append(cur)
            res.append(j)
        res = tmp + res    
        return res         
