class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("stack is empty.")
        return self.items[-1]

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.items[pos]
            pos += 1

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    stack = Stack()
    print("Length:", len(stack))
    print("Is Empty:", stack.is_empty())

    N=4
    print("Push from 1 to", N)
    for i in range(1, N + 1):
        print("Push:", i)
        stack.push(i)
        print("Len:", len(stack), "Stack:", stack)
        print("Peek:", stack.peek())
    print("Is Empty:", stack.is_empty())
    for i in stack:
        print("Element:", i)
    print()
    for i in range(N):
        print("Peek and Pop: ", stack.peek())
        stack.pop()
        print("Stack:", stack)

    print("Length:", len(stack))
    print("Is Empty:", stack.is_empty())

'''
Length: 0
Is Empty: True
Push from 1 to 4
Push: 1
Len: 1 Stack: [1]
Peek: 1
Push: 2
Len: 2 Stack: [1, 2]
Peek: 2
Push: 3
Len: 3 Stack: [1, 2, 3]
Peek: 3
Push: 4
Len: 4 Stack: [1, 2, 3, 4]
Peek: 4
Is Empty: False
Element: 1
Element: 2
Element: 3
Element: 4

Peek and Pop:  4
Stack: [1, 2, 3]
Peek and Pop:  3
Stack: [1, 2]
Peek and Pop:  2
Stack: [1]
Peek and Pop:  1
Stack: []
Length: 0
Is Empty: True
'''