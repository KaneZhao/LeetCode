"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
# Use dictionary to count the number of characters
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in ransomNote:
            if j in dic and dic[j] >= 1:
                dic[j] -= 1
            else:
                return False
        return True            

