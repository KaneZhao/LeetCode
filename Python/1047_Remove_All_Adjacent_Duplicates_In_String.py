"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:      
        lst = list(s)
        i = j = 0
        while j < len(s):
            lst[i] = lst[j]
            if i > 0 and lst[i] == lst[i - 1]:
                i -= 1
            else:
                i += 1
            j += 1
        return ''.join(lst[:i])                     

"""
class Solution:
    def removeDuplicates(self, s: str) -> str:      
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)        
        s = ''.join(stack)  
        return s           
"""