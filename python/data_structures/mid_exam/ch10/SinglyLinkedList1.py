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


class SinglyLinkedList:
    def __init__(self):
        self.head = self.next_ = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_ is not None:
            temp = self.head
            self.next_ = self.next_.next
            return temp
        else:
            raise StopIteration
        # iterator = self.head
        #
        # temp = self.head
        # num = 0
        # while temp is self.next_:
        #     temp = temp.next
        #     num += 1
        #
        # # while iterator.item != self.next_.item:
        # new_num = 0
        # while new_num <= num:
        #     result = iterator
        #     iterator = iterator.next
        #     print(new_num)
        #     print(iterator)
        #     new_num += 1
        #     return result
        # else:
        #     raise StopIteration

    def add_head(self, node_new):
        new_node = Node(node_new)

        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.head is None:
            self.head = new_node
        else:
            # 이거로 변경하면 앞부분은 되고 뒷부분은 안된다.
            # self.next_.next = new_node
            # self.next_ = new_node

            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def delete_tail(self):
        if (self.head != None):

            # 1. if head in not null and next of head
            #   is null, release the head
            if (self.head.next == None):
                self.head = None
            else:

                # 2. Else, traverse to the second last
                #   element of the list
                temp = self.head
                while (temp.next.next != None):
                    temp = temp.next

                # 3. Change the next of the second
                #   last node to null and delete the
                #   last node
                lastNode = temp.next
                temp.next = None
                lastNode = None

        # if self.head is self.next_:
        #     self.next_ = self.head = None
        # else:
        #     temp = self.head
        #     while temp.next.next is not None:
        #         temp = temp.next
        #     self.next_ = temp
        #     temp.next = None



            # temp = self.head
            # while temp.next.next is not None:
            #     temp = temp.next
            #
            # lastNode = temp.next
            # temp.next = None
            # lastNode = None


    def delete_head(self):
        # if self.head is not self.next_:
        #     self.next_ = self.head = None
        # else:
        #     self.head = self.head.next

        if self.head is not None:
            temp = self.head

            self.head = self.head.next

            temp = None

    def insert_after(self, node, node_new):
        new_node = Node(node_new)

        temp = self.head
        num = 0
        while temp is node:
            temp = temp.next
            num += 1

        if num == 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            for _ in range(num):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node


        # new_node = Node(node_new)
        #
        # if node is self.next_:
        #     self.next_.next = new_node
        #     self.next_ = new_node
        # else:
        #     new_node.next = node.next
        #     node.next = new_node

    def insert_before(self, node, node_new):
        new_node = Node(node_new)

        temp = self.head
        num = 0
        while temp is node:
            temp = temp.next
            num += 1

        temp = self.head
        if num == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(num):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                temp.next = new_node
                new_node.next = temp.next.next


        # if self.head is node:
        #     new_node.next = self.head
        #     self.head = new_node
        # else:
        #     temp = self.head
        #     num = 0
        #     while temp is node:
        #         temp = temp.next
        #         num += 1
        #
        #     for i in range(0, num):
        #         if(temp != None):
        #             temp = temp.next

        # new_node = Node(node_new)
        #
        # if node is self.head:
        #     new_node.next = self.head
        #     self.head = new_node
        # else:
        #     self.head = new_node
        #     new_node.next = node

    def __str__(self):
        result = "["
        iterator = self.head

        while iterator is not None:
            result += str(iterator)
            iterator = iterator.next

            if iterator is not None:
                result += ", "

        result += "]"
        return result



list_ = SinglyLinkedList()
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

for i in list_:
    print("Element:", i)

list_.add_tail(Node(700))
print("7", list_)

list_.insert_after(Node(50), Node(250))
print("8", list_)

list_.insert_before(Node(50), Node(750))
print("9", list_)

for i in list_:
    print("Element:", i)
