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

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear += 1

        self.arr[self.rear] = elem

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        self.arr[self.front] = None
        if self.front == self.rear and self.front != -1:
            self.front = self.rear = -1
        else:
            self.front += 1

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.arr[self.front]

    # empty인 경우는 0하고 연산식에 따르면 1이 남는다 그래서
    # 둘다 -1인 경우는 0으로 처리한다.
    def __len__(self):
        return 0 if self.is_empty() else self.rear - self.front + 1

    def __iter__(self):
        pos = 0
        while pos < len(self):
            yield self.arr[pos]
            pos += 1

    def __str__(self):
        return str(self.arr)