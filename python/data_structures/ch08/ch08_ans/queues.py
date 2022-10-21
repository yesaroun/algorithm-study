from arrays import Array

class Queue:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.front = self.rear = -1

    def is_full(self):
        return self.rear >= self.capacity - 1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def enqueue(self, elem):
        if self.is_full():
            raise Exception("Queue is full")

        self.rear += 1
        self.arr[self.rear] = elem

        if self.front < 0:
            self.front = 0

    def __str__(self):
        return str(self.arr)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        # 필요하다면 None 설정
        self.arr[self.front] = None
        if self.front == self.rear and self.front != -1:
            self.front = self.rear = -1
        else:
            self.front += 1

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.arr[self.front]

    def __len__(self):
        # return self.capacity - self.arr.items.count(None)
        return 0 if self.is_empty() else self.rear - self.front + 1

    def __iter__(self):
        if self.is_empty:
            return

        pos = self.front
        while pos <= self.rear:
            yield self.arr[pos]
            pos += 1


if __name__ == "__main__":
    N = 5
    q = Queue(N)
    print("Length:", len(q))
    print("Empty:", q.is_empty())
    print("Enqueue 1 -", N)

    for i in range(1, N + 1):
        q.enqueue(i)
        print("Peeking:", q.peek())
        print("Queue =", q)

    print("Length:", len(q))
    print("Empty:", q.is_empty())

    while not q.is_empty():
        print("Peeking:", q.peek())
        q.dequeue()
        print("Queue =", q)

    print("Length:", len(q))
    print("Empty:", q.is_empty())

"""
Length: 0
Empty: True
Enqueue 1 - 5
Peeking: 1
Queue = [1, None, None, None, None]
Peeking: 1
Queue = [1, 2, None, None, None]
Peeking: 1
Queue = [1, 2, 3, None, None]
Peeking: 1
Queue = [1, 2, 3, 4, None]
Peeking: 1
Queue = [1, 2, 3, 4, 5]
Length: 5
Empty: False
Peeking: 1
Queue = [None, 2, 3, 4, 5]
Peeking: 2
Queue = [None, None, 3, 4, 5]
Peeking: 3
Queue = [None, None, None, 4, 5]
Peeking: 4
Queue = [None, None, None, None, 5]
Peeking: 5
Queue = [None, None, None, None, None]
Length: 0
Empty: True
"""
