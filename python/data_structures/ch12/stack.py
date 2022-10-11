from data_structures.ch12.SinglyLinkedList import SinglyLinkedList

class Stack:
    def __init__(self):
        self.list_ = SinglyLinkedList()

    def push(self, elem):
        self.list_.add_head(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")

        self.list_.delete_tail()

    def is_empty(self):
        return not self.list_

    def __iter__(self):
        raise NotImplemented

    def __str__(self):
        return str(self.list_)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack)

    print("peek:", stack.peek())
    stack.pop()
    print(stack)
    stack.push(30)
    print(stack)
    stack.push(40)
    print(stack)
    print("peek:", stack.peek())
    stack.pop()
    print(stack)

    for i in stack:
        print("Element:", i)

    print()
    print(stack)
    while not stack.is_empty():
        print("peek:", stack.peek())
        stack.pop()
        print(stack)

"""
[20, 10] 
peek: 20 
[10]
[30, 10] 
[40, 30, 10] 
peek: 40 
[30, 10] 
Element: 30 
Element: 10
[30, 10] 
peek: 30 
[10] 
peek: 10 
[]
"""