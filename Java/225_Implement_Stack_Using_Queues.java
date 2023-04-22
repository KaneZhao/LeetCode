/**
 Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

 Implement the MyStack class:

 void push(int x) Pushes element x to the top of the stack.
 int pop() Removes the element on the top of the stack and returns it.
 int top() Returns the element on the top of the stack.
 boolean empty() Returns true if the stack is empty, false otherwise.

 using only one queue
 */
class MyStack {

    private Queue<Integer> queue = new LinkedList<>();
    
    public MyStack() {
        
    }
    
    public void push(int x) {
        queue.add(x);
    }
    
    public int pop() {
        for (int i = 0; i < queue.size() - 1; ++i){
            queue.add(queue.remove());
        }
        return queue.remove();
    }
    
    public int top() {
        for (int i = 0; i < queue.size() - 1; ++i){
            queue.add(queue.remove());
        }
        int res = queue.peek();
        queue.add(queue.remove());
        return res;    
    }
    
    public boolean empty() {
        return queue.isEmpty();  
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */