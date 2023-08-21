"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(-1)  
        self.len = 0     

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        else:
            cur, path = self.dummy.next, index
            while path > 0:
                cur = cur.next
                path -= 1
            return -1 if cur is None else cur.val    
                
    def addAtHead(self, val: int) -> None:   
        self.dummy.next = ListNode(val, self.dummy.next)        
        self.len += 1

    def addAtTail(self, val: int) -> None:
        pre = self.dummy
        while pre.next is not None:
                pre = pre.next
        pre.next = ListNode(val)
        self.len += 1           

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len:
            self.addAtTail(val)
        elif index < self.len:
            pre = self.dummy
            while index:
                pre = pre.next
                index -= 1
            pre.next = ListNode(val, pre.next)    
            self.len += 1    

    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index < self.len:
            pre = self.dummy
            while index:
                pre = pre.next
                index -= 1
            pre.next = pre.next.next 
            self.len -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)