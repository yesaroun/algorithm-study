from circular_doubly_linked_list import CircularDoublyLinkedList, Node

class Queue:
    def __init__(self):
        self.list_ = CircularDoublyLinkedList()

    def enqueue(self, elem):
        node = Node(elem)
        self.list_.add_tail(node)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        self.list_.delete_head()

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.list_.head

    def is_empty(self):
        return self.list_.is_empty()

    def __iter__(self):
        return iter(self.list_)

    def __str__(self):
        return str(self.list_)


if __name__ == "__main__":

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue)

    print("peek:", queue.peek())
    queue.dequeue()
    print(queue)

    queue.enqueue(30)
    print(queue)
    queue.enqueue(40)
    print(queue)
    print("peek:", queue.peek())
    queue.dequeue()
    print(queue)

    for i in queue:
        print("Element:", i)
