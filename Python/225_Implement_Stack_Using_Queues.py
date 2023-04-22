"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.

Using two queue
"""
class MyStack:

    # q2 have size 1 and store top of the stack
    # q1 store rest of the elements
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if self.q2:
            self.q1.append(self.q2.pop(0))
        self.q2.append(x)    
    
    # if q2 is not empty, just return data of q2
    # otherwise continuously pop from the front and push to the back, we can find the last element of q1
    def pop(self) -> int:
        if self.q2:
            return self.q2.pop(0)
        else:
            for _ in range(len(self.q1) - 1):
                self.q1.append(self.q1.pop(0))
            return self.q1.pop(0)    

    def top(self) -> int:
        if self.q2:
            return self.q2[0]
        else:
            for _ in range(len(self.q1) - 1):
                self.q1.append(self.q1.pop(0))
            res = self.q1[0]
            self.q1.append(self.q1.pop(0))
            return res   

    def empty(self) -> bool:
        return not self.q1 and not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()