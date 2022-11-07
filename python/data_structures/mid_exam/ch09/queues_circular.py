from arrays import Array

class Queue:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.capacity = capacity
        self.arr = Array(self.capacity)
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    # 더 조건 필요할 듯?
    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty.")
        return self.arr[self.front]

    # 확인하기
    def __len__(self):
        if self.is_empty():
            return 0
        if self.rear < self.front:
            return self.capacity - self.front + self.rear + 1
        return self.rear - self.front + 1

    def __str__(self):
        return str(self.arr)

    # iter는 그냥 리스트를 내 용량만큼 돌면 순서대로 안나온다
    # front에서 rear를 계산 해야 한다.
    # iter의 경우 이전에는 용량만큼 돌았는데 그때는 항상 앞에서 부터 시작했으니까 괜찮은데 이제는 안된다
    def __iter__(self):
        pos = self.front
        for i in range(pos, pos + len(self)):
            yield self.arr[i % self.capacity]

    # 확인하기
    def enqueue(self, elem):
        if self.is_full():
            raise Exception("Queue is full")

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = elem

        if self.front < 0:
            self.front += 1

    #
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        self.arr[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
            return

        self.front # 추가해야함


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

