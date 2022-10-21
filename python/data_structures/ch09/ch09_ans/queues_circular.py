from arrays import Array

class Queue:

    CAPACITY = 10
    def __init__(self, capacity=CAPACITY):
        self.capacity = capacity
        self.arr = Array(self.capacity)
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.arr[self.front]

    def __len__(self):
        if self.is_empty():
            return 0

        if self.rear < self.front:
            return self.capacity - self.front + self.rear + 1

        return self.rear - self.front + 1

    def __iter__(self):
        pos = self.front

        for i in range(pos, pos + len(self)):
            yield self.arr[i % self.capacity]

    def __str__(self):
        return str(self.arr)

    def enqueue(self, elem):
        if self.is_full():
            raise Exception("queue is full.")

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = elem

        if self.front < 0:
            self.front += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty.")

        self.arr[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
            return
        
        self.front = (self.front + 1) % self.capacity



if __name__ == "__main__":
    N = 8
    queue = Queue(N)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    print(queue)
    print("Peek:", queue.peek())
    queue.dequeue()
    print("Peek:", queue.peek())
    queue.dequeue()
    print(queue)
    queue.enqueue("E")
    queue.enqueue("F")
    queue.enqueue("G")
    queue.enqueue("H")
    queue.enqueue("I")
    queue.enqueue("J")
    print(queue)
    queue.dequeue()
    print(queue)
    for i in queue:
        print("Element:", i)
    print("Peek:", queue.peek())

    while not queue.is_empty():
        queue.dequeue()
    print(queue)
"""
['A', 'B', 'C', 'D', None, None, None, None]
Peek: A
Peek: B
[None, None, 'C', 'D', None, None, None, None]
['I', 'J', 'C', 'D', 'E', 'F', 'G', 'H']
['I', 'J', None, 'D', 'E', 'F', 'G', 'H']
Element: D
Element: E
Element: F
Element: G
Element: H
Element: I
Element: J
Peek: D
[None, None, None, None, None, None, None, None]
"""