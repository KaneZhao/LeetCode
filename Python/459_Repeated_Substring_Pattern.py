"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i, slen = 1, len(s)
        while i <= slen // 2:
            if slen % i == 0:
                if s[0:i] * (slen // i) == s:
                    return True
            i += 1
        return False             