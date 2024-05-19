class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        # 처음에만 head가 new node를 가리키도록
        if self.head is None:
            self.head = new_node
        # 맨 뒤에 node가 new_node를 가리켜야 한다.
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def inset(self, idx, value):
        pass



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.get(0)
ll.get(1)
ll.get(3)

