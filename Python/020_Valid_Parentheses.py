"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if len(stack) == 0 or dic[i] != stack[-1]:
                    return False
                else:
                    stack.pop()     
        return len(stack) == 0           