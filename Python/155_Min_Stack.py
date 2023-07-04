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
        self.min_val = None

    def push(self, val: int) -> None:
        if len(self.s1) == 0:
            self.s1.append(val)
            self.min_val = val
        else:
            if val < min_val:
                self.s1.append(self.min_val)
                self.min_val = val
            else:
                self.s1.append(val)    

    def pop(self) -> None:
        if len(self.s1) == 0:
            raise IndexError()
        else:
            top = self.s1.pop()
            self.min_val = min(top, self.)   
        
    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.min_val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()