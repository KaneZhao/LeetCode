"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start, track, tar):
            if tar == 0:
                res.append(track[:])
                return
            if tar < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                track.append(candidates[i])
                backtrack(i + 1, track, tar - candidates[i])
                track.pop()        
        backtrack(0, [], target)
        return res        