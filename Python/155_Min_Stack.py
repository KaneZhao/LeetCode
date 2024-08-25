"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        if len(self.s1) == 0:
            self.s2.append(val)
        else:
            top = self.s2[-1]
            if top < val:
                self.s2.append(top)
            else:
                self.s2.append(val) 
        self.s1.append(val)               

    def pop(self) -> None:
        if len(self.s1) == 0:
            raise IndexError()
        else:
            self.s1.pop()
            self.s2.pop()    
        
    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.s2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()