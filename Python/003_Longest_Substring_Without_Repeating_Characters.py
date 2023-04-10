"""
Given a string s, find the length of the longest 
substring without repeating characters.

hints: using sliding window
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        windows = {}    
        left, right, res = 0, 0, 0
        while right < len(s):
            cur = s[right]
            if cur in windows:
                left = left if left > windows[cur] + 1 else windows[cur] + 1
            windows[cur] = right
            res = res if res >= right - left + 1 else right - left + 1
            right += 1
        return res    


