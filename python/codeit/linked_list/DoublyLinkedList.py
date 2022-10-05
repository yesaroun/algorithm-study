class Node:
    """더블리 링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """더블리 링크드 리스트"""
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        """연결 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        # 코드를 쓰세요.
        new_node = Node(data) # 새로운 노드 생성

        # head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 이미 노드가 있으면
        else:
            new_node.next = self.head # 새로운 노드의 다음 노드를 head 노드로 지정
            self.head.prev = new_node # head 노드의 전 노드를 새로운 노드로 지정
            self.head = new_node # head 노드 업데이트

    def insert_after(self, previous_node, data):
        """주어진 노드 다음에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)  # 새로운 노드 생성

        # tail 노드 다음에 노드를 삽입할 때
        if previous_node is self.tail:
            self.tail.next = new_node  # 새로운 노드를 tail 노드의 다음 노드로 지정한다
            new_node.prev = self.tail  # tail 노드를 새로운 노드의 전 노드로 지정한다
            self.tail = new_node  # 새로운 노드를 tail 노드로 지정한다

        else:
            # 새롭게 생성한 노드를 이미 있는 링크드 리스트에 연결시키고
            new_node.prev = previous_node
            new_node.next = previous_node.next

            # 이미 있는 노드들의 앞과 다음 레퍼런스를 새롭게 생성한 노드로 지정한다
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)   # 새로운 데이터를 저장하는 노드

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:       # 링크드 리스트에 데이터가 이미 있는 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다."""

        iterator = self.head        # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # index 번째 있는 노드로 간다.
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고 있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다."""
        iterator = self.head        # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다.
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다.
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next    # 다음 노드로 넘어간다.

        return res_str


# 빈 링크드 리스트 정의
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)
#--==>> | 2 | 3 | 5 | 7 |