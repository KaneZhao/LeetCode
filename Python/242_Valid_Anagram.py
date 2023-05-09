"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1    
        for j in t:
            if j in dic and dic[j] > 0:
                dic[j] -= 1
            else:
                return False    
        return True            