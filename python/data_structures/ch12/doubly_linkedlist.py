class Node:
    def __init__(self, item=None):
        self.item = item
        self.rlink = self.llink = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True

    def __str__(self):
        return f"{self.item}"

class DoublyLinkedList:
    def __init__(self):
        self.tail = None

    def add_head(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
            new_node.rlink = self.tail
            new_node.llink = self.tail
        else:
            new_node.rlink = self.tail.rlink
            self.tail.rlink.llink = new_node
            new_node.llink = self.tail
            self.tail.rlink = new_node

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
            new_node.rlink = new_node.llink = self.tail
        else:
            new_node.rlink = self.tail.rlink
            self.tail.rlink.llink = new_node
            new_node.llink = self.tail
            self.tail.rlink = new_node
            self.tail = new_node

    def delete_tail(self):
        if self.tail is not None:
            if self.tail == self.tail.rlink == self.tail.llink:
                self.tail = None
            else:
                self.tail.llink.rlink = self.tail.rlink
                self.tail.rlink.llink = self.tail.llink
                self.tail = self.tail.llink
        else:
            raise Exception

    def delete_head(self):
        if self.tail is not None:
            if self.tail == self.tail.llink == self.tail.rlink:
                self.tail = None
            else:
                head = self.tail.rlink
                self.tail.rlink = head.rlink
                head.rlink.llink = self.tail
        else:
            raise Exception

    def insert_after(self, node, node_new):
        new_node = Node(node_new)

        temp = self.tail

        while str(temp.rlink) != str(node):
            temp = temp.rlink
        # temp.rlink 가 node

        if temp.rlink is self.tail:
            new_node.rlink = self.tail.rlink
            new_node.llink = self.tail
            self.tail.rlink.llink = new_node
            self.tail.rlink = new_node
            self.tail = new_node
        else:
            new_node.rlink = temp.rlink.rlink
            new_node.llink = temp.rlink
            temp.rlink.rlink.llink = new_node
            temp.rlink.rlink = new_node

    def insert_before(self, node, node_new):
        new_node = Node(node_new)

        temp = self.tail

        while str(temp.rlink) != str(node):
            temp = temp.rlink
        # temp.rlink 가 node

        new_node.rlink = temp.rlink
        new_node.llink = temp
        temp.rlink.llink = new_node
        temp.rlink = new_node


    def __str__(self):

        if self.tail is not None:
            result = "["

            iterator = self.tail.rlink

            result += str(iterator)
            if self.tail is not iterator:
                result += ", "
            iterator = iterator.rlink

            while iterator is not self.tail.rlink:
                result += str(iterator)
                iterator = iterator.rlink

                if iterator is not self.tail.rlink:
                    result += ", "

            result += "]"

            return result

        else:
            return "[]"

list_ = DoublyLinkedList()
list_.add_head(Node(50))
list_.add_tail(Node(100))
list_.add_tail(Node(150))
print("1", list_)


list_.delete_head()
print("2", list_)
list_.delete_tail()
print("3", list_)
list_.delete_head()
print("4", list_)

list_.add_tail(Node(150))
list_.insert_before(Node(150), Node(999))
print("5", list_)

list_.add_head(Node(50))
list_.add_tail(Node(100))
print("6", list_)

list_.add_tail(Node(700))
print("7", list_)

list_.insert_after(Node(50), Node(250))
print("8", list_)

list_.insert_before(Node(50), Node(750))
print("9", list_)