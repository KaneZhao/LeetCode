"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        lst = list(s)
        vowels = 'aeiouAEIOU'
        i, j = 0, len(s) - 1   
        while i < j:
            # Move the i, j pointer until we find a vowel
            if lst[i] not in vowels: 
                i += 1
                continue
            if lst[j] not in vowels:
                j -= 1
                continue
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        return ''.join(lst)                  
        