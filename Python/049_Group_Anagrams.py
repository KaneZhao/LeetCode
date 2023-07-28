"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""
Build a dictionary to store sortd string as key and list of real string as value, then return the dic values
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res, dic = [], {}
        for c in strs:
            tmp = ''.join(sorted(c))
            if tmp in dic:
                dic[tmp].append(c)
            else:
                dic[tmp] = [c]

        return list(dic.values())           
            