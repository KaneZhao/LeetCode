"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
import heapq as hq

class Solution:
    def sort_key(self, x):
        return x[1]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        res = list(dic.items())
        hq.heapify(res)
        return [x[0] for x in hq.nlargest(k, res, self.sort_key)]    