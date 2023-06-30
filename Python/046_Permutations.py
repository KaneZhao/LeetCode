"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nlen = len(nums)
        track, res = [], []
        def helper(lst, track):
            if len(track) == nlen:
                res.append(track[:])
                return 
            for i in range(len(nums)):
                tmp = nums[i]
                track.append(tmp)
                nums.pop(i)
                helper(lst, track)
                nums.insert(i, tmp)
                track.pop()    
        helper(nums, track)
        return res      