class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        # 가장 마지막 순서 삽입
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:   # 두 노드 사이에 삽입
            new_node.next = previous_node.next
            previous_node.next = new_node

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # 링크드 리스트 전체를 돈다
        while iterator is not None:
            # iterator 노드의 데이터가 찾는 데이터면 iterator를 리턴한다
            if iterator.data == data:
                return iterator
            iterator = iterator.next  # 다음 노드로 넘어간다

        # 링크드 리스트 안에 원하는 데이터가 없었기 때문에 None 리턴한다
        return None


    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 마지막에 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)

print(linked_list)
#--==>> | 2 | 3 | 5 | 7 |

node_2 = linked_list.find_node_with_data(2)     # 인덱스 2에 있는 노드 접근
linked_list.insert_after(node_2, 6)             # 인덱스 2 뒤에 6 삽입

print(linked_list)
#--==>> | 2 | 6 | 3 | 5 | 7 |

head_node = linked_list.head    # 헤드 노드 접근
linked_list.insert_after(head_node, 9)  # 헤드 노드 뒤에 9 삽입

print(linked_list)
#--==>> | 2 | 9 | 6 | 3 | 5 | 7 |