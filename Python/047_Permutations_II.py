"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(lst, track):
            if lst == []:
                res.append(track[:])
                return
            for i in range(len(lst)):
                if i > 0 and lst[i] == lst[i - 1]:
                    continue 
                tmp = lst[i]
                track.append(tmp)
                lst.pop(i)
                backtrack(lst, track)
                lst.insert(i, tmp)
                track.pop()
        backtrack(nums, [])
        return res

