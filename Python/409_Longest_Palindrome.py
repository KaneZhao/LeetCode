"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = dict()
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        flg, res = False, 0
        for k, v in dic.items():
            if v % 2:
                res += v - 1
                flg = True
            else:
                res += v    
        return res + 1 if flg else res  
    

# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         dic = dict()
#         for i in s:
#             dic[i] = dic.get(i, 0) + 1
#         odd_len = len([v for k, v in dic.items() if v % 2])  
#         return len(s) if odd_len == 0 else len(s) - odd_len + 1    

        