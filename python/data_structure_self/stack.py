class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            current_node = self.top
            self.top = self.top.next
            return current_node.item

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.item


stack = Stack()
stack.push(1)
print(stack.peek())  # 1
stack.push(2)
print(stack.peek())  # 2
stack.pop()
print(stack.peek())  # 1
stack.pop()
print(stack.peek())  # None
