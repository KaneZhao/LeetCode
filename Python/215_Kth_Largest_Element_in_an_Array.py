"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""
import heapq as hq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq.heapify(nums)
        return hq.nlargest(k, nums)[-1]