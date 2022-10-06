class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True

        return False

    def __str__(self):
        return f"{self.item}"

class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None

    def add_head(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.tail is None:
            self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = self.tail.next

    def delete_tail(self):
        if self.tail is not None:
            temp = self.tail.next   # head
            while temp is not self.tail:
                temp = temp.next

            temp.next = self.tail.next
            self.tail = temp

    def delete_head(self):
        if self.tail is not None:
            self.tail.next = self.tail.next.next

    def insert_after(self, node, node_new):
        new_node = Node(node_new)

        if node is self.tail:
            new_node.next = self.tail.next
            self.tail.next = new_node
        elif node is self.tail.next:
            self.tail.next.next = new_node
        else:
            new_node.next = node.next
            node.next = new_node


    def insert_before(self, node, node_new):
        new_node = Node(node_new)

        if node is self.tail:
            temp = self.tail.next  # temp = head
            while temp is not self.tail:
                temp = temp.next
            # temp = tail.prev

            new_node.next = self.tail
            temp.next = new_node
        elif node is self.tail.next:
            new_node.next = self.tail.next
            self.tail.next = new_node
        else:
            temp = self.tail.next   # temp = head
            while temp is not node:
                temp = temp.next
            # temp = node.prev

            new_node.next = node
            temp.next = new_node


    def delete(self, node):
        temp = self.tail.next
        temp_prev = self.tail
        while temp is not node:
            temp = temp.next
            temp_prev = temp_prev.next

        temp_prev.next = temp.next

    def __str__(self):
        result = "["
        iterator = self.tail.next

        if iterator is not None:
            result += str(iterator)
            if iterator.next is not None:
                result += ", "
            iterator = iterator.next

        while iterator is not self.tail.next:
            result += str(iterator)
            iterator = iterator.next

            if iterator is not self.tail.next:
                result += ", "

        result += "]"
        return result



list_ = CircularSinglyLinkedList()
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
#list_.insert_before(Node(150), Node(999))
print("5", list_)

list_.add_head(Node(50))
list_.add_tail(Node(100))
print("6", list_)

list_.add_tail(Node(700))
print("7", list_)

list_.insert_after(Node(50), Node(250))
print("8", list_)

# list_.insert_before(Node(50), Node(750))
print("9", list_)