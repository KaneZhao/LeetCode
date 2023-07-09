"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

"""
Perform a while loop now, with the condition that either i or j should be greater than or equal to 0. 
Inside this loop, perform another while loop on string S. 
The condition for this loop is that when i is greater than or equal to 0 and the current character is a hash symbol (#), or cnt1 is greater than 0, if the current character is a backspace, increment cnt1; otherwise, decrement cnt1. 
Then, decrement i. This way, the current character is skipped, and there is no need to perform a comparison
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        cnti, cntj = 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and (s[i] == '#' or cnti > 0):
                if s[i] == '#':
                    cnti += 1
                else:
                    cnti -= 1
                i -= 1 
            while j >= 0 and (t[j] == '#' or cntj > 0):
                if t[j] == '#':
                    cntj += 1
                else:
                    cntj -= 1
                j -= 1
            if i < 0 or j < 0:
                return i == j
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1                       
        return i == j                              

       
# # using stack:
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         s1, s2 = [], []
#         for i in s:
#             if i == '#':
#                 if s1:
#                     s1.pop()
#             else:
#                 s1.append(i)
        
#         for i in t:
#             if i == '#':
#                 if s2:
#                     s2.pop()
#             else:
#                 s2.append(i)
        
#         return s1 == s2                      