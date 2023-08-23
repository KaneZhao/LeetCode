"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slen, i = len(s), 0
        lst = list(s)
        if k >= slen:
            return s[::-1]
        while i < slen:
            self.reverse(lst, i, i + k - 1) 
            i += 2 * k   
        return ''.join(lst)    

    def reverse(self, s, i, j):
        j = min(j, len(s) - 1)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1          
