"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, track = [], []
        def helper(start, n, k):
            if len(track) == k:
                res.append(track[:])
                return
            for i in range(start, n + 1):
                track.append(i)
                helper(i + 1, n, k)
                track.pop()
        helper(1, n, k)
        return res