"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res, i = [], 0
        plist, curlist = [0] * 26, [0] * 26
        for j in p:
            plist[ord(j) - ord('a')] += 1
        for k in range(len(p)):   
            curlist[ord(s[k]) - ord('a')] += 1
        while i + len(p) <= len(s):
            if i > 0:
               curlist[ord(s[i - 1]) - ord('a')] -= 1 
               curlist[ord(s[i + len(p) - 1]) - ord('a')] += 1 
            if plist == curlist:
                res.append(i)
            i += 1
        return res        
