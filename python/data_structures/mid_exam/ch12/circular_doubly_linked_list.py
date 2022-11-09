class Node:
    def __init__(self, item=None):
        self.item = item
        self.llink = self.rlink = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True
        return False

    def __str__(self):
        return f"{self.item}"

    def __repr__(self):
        return str(self)

class CircularDoublyLinkedList:
    """class_ Doubly linked list"""

    def __init__(self):
        self.head = None

    def add_head(self, node_new):
        """head 추가 연산 메소드"""
        new_node = Node(node_new)

        if self.head is None:
            self.head = new_node
            new_node.rlink = new_node.llink = self.head
        else:
            new_node.llink = self.head.llink
            self.head.llink.rlink = new_node
            new_node.rlink = self.head
            self.head.llink = new_node
            self.head = new_node

    def add_tail(self, node_new):
        """tail 추가 연산 메소드"""
        new_node = Node(node_new)

        if self.head is None:
            self.head = new_node
            new_node.rlink = new_node.llink = self.head
        else:
            new_node.llink = self.head.llink
            self.head.llink.rlink = new_node
            new_node.rlink = self.head
            self.head.llink = new_node

    def delete_head(self):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            if self.head == self.head.llink == self.head.rlink:
                self.head = None
            else:
                self.head.llink.rlink = self.head.rlink
                self.head.rlink.llink = self.head.llink
                self.head = self.head.rlink

    def delete_tail(self):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            if self.head == self.head.llink == self.head.rlink:
                self.head = None
            else:
                tail = self.head.llink
                tail.llink.rlink = self.head
                self.head.llink = tail.llink

    def insert_after(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            new_node = Node(node_new)
            temp = self.head

            while str(temp) != str(node):
                temp = temp.rlink
            # temp가 node

            new_node.rlink = temp.rlink
            new_node.llink = temp
            temp.rlink.llink = new_node
            temp.rlink = new_node


    def insert_before(self, node, node_new):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            new_node = Node(node_new)
            temp = self.head

            while str(temp) != str(node):
                temp = temp.rlink
            # temp가 node

            if temp is self.head:
                new_node.rlink = self.head
                new_node.llink = self.head.llink
                self.head.llink.rlink = new_node
                self.head.llink = new_node
                self.head = new_node
            else:
                new_node.rlink = temp
                new_node.llink = temp.llink
                temp.llink.rlink = new_node
                temp.llink = new_node

    def delete(self, node):
        if self.is_empty():
            raise Exception("list is empty.")
        else:
            temp = self.head

            while str(temp) != str(node):
                temp = temp.rlink
            # temp가 node

            if temp is self.head:
                self.head = temp.rlink

            temp.rlink.llink = temp.llink
            temp.llink.rlink = temp.rlink

    def __iter__(self):
        self.current = self.head.llink
        self.count = 0
        return self


    def __next__(self):
        self.current = self.current.rlink
        if self.current is self.head and self.count == 1:
            raise StopIteration
        if self.current is self.head and self.count == 0:
            self.count += 1

        return self.current

    def is_empty(self):
        return not self.head

    def __str__(self):
        if self.head is not None:
            result = "["

            iterator = self.head

            result += str(iterator)
            if self.head.llink is not iterator:
                result += ", "
            iterator = iterator.rlink

            while iterator is not self.head:
                result += str(iterator)
                iterator = iterator.rlink

                if iterator is not self.head:
                    result += ", "

            result += "]"

            return result

        else:
            return "[]"

if __name__ == "__main__":
    list_ = CircularDoublyLinkedList()
    list_.add_tail(Node(10))
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
    print(list_)
    for i in list_:
        print("Element:", i)
    print()
    it = iter(list_)
    while True:
        try:
            i = next(it)
        except StopIteration:
            break
        print("Element:", i)

    print(list_)
    while not list_.is_empty():
        list_.delete_tail()
        print(list_)
    list_.add_tail(Node(20))
    list_.add_head(Node(30))
    print(list_)
    list_.insert_after(Node(30), Node(40))
    list_.insert_before(Node(20), Node(10))
    print(list_)
    list_.delete(Node(40))
    print(list_)
    list_.delete(Node(30))
    print(list_)
    list_.delete(Node(20))
    print(list_)