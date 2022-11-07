from arrays import Array

class Stack:
    CAPACITY = 10

    def __init__(self, capacity = CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.top = -1

    def is_full(self):
        return len(self) >= self.capacity

    def is_empty(self):
        return len(self) <= 0

    def push(self, elem):
        if self.is_full():
            raise Exception("stack is full.")

        self.top += 1
        self.arr[self.top] = elem

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty.")

        self.arr[self.top] = None
        # self.arr[len(self) - 1] = None
        self.top -= 1

    def peek(self):
        if self.is_empty():
            raise Exception("stack is full.")

        # return self.arr[len(self) - 1]
        return self.arr[self.top]

    def __len__(self):
        return self.top + 1

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1

    def __str__(self):
        return str(self.arr)


if __name__ == "__main__":
    N = 4
    stack = Stack(N)

    print("Length:", len(stack))
    print("Is Empty:", stack.is_empty())
    print("Push from 1 to", N)
    for i in range(1, N + 1):
        print("Push:", i)
        stack.push(i)
        print("Stack:", stack)
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
"""
Length: 0
Is Empty: True
Push from 1 to 4
Push: 1
Stack: [1, None, None, None]
Peek: 1
Push: 2
Stack: [1, 2, None, None]
Peek: 2
Push: 3
Stack: [1, 2, 3, None]
Peek: 3
Push: 4
Stack: [1, 2, 3, 4]
Peek: 4
Is Empty: False
Element: 1
Element: 2
Element: 3
Element: 4

Peek and Pop:  4
Stack: [1, 2, 3, None]
Peek and Pop:  3
Stack: [1, 2, None, None]
Peek and Pop:  2
Stack: [1, None, None, None]
Peek and Pop:  1
Stack: [None, None, None, None]
Length: 0
Is Empty: True
"""