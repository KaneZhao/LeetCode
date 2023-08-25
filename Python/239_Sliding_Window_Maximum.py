"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)  

    def front(self):
        return self.queue[0]          

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()
        res = []
        for i in range(k):
            queue.push(nums[i])
        res.append(queue.front())
        for i in range(k, len(nums)):
            queue.pop(nums[i - k])
            queue.push(nums[i])
            res.append(queue.front())
        return res        