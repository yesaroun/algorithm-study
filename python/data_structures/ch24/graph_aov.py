from stacks import Stack

def read_input(name_file="input.dat"):
    mat = []
    with open(name_file) as f:
        for line in f:
            (*row,) = map(int, line.split())
            mat.append(row)
    return mat

def print_mat(mat):
    rows, cols = len(mat), len(mat[0])
    for row in range(rows):
        for col in range(cols):
            print(f"{mat[row][col]}", end=" ")
        print("\b")

class HeadNode:
    def __init__(self, id_=0, indegree=0):
        self.id_ = id_
        self.indegree = indegree
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.id_}"


class Node:
    def __init__(self, vertex=0):
        self.vertex = vertex
        self.link = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.vertex}"


class GraphAovBuilder:
    @staticmethod
    def build(mat):
        if not mat:
            raise Exception("the mat should not be none.")

        size = len(mat)
        # print("size: ", size) # 9
        # Node(i) 는 Adjacency list 의 head 이다.
        list_ = [HeadNode(i) for i in range(size)]
        # print("list_: ", list_) #--==>> list_:  [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # 이 id로 HeadNode 객체들이 생성된다

        # 18page : V0~8 하나에 연결되는 노드 생성
        for row in range(size):
            prev = list_[row]
            for col in range(size):
                # 0이면 지나간다
                if not mat[row][col]:
                    continue

                node = Node(col)
                prev.link = node
                prev = node

        return list_


class GraphAov:
    def __init__(self, list_, mat):
        self.list_ = list_
        self.mat = mat
        self.__build_indegree()

    def indegree(self, v):
        ret = 0
        for row in range(len(self.mat)):
            ret += self.mat[row][v]
        return ret

    def outdegree(self, v):
        return sum(self.mat[v])

    def __build_indegree(self):
        for i, v in enumerate(self):
            v.indegree = self.indegree(i)

    def sort_topology(self):
        ret = []  # for return
        self.__build_indegree()

        stack = Stack()
        # indegree 0 인 노드들을 stack 에 추가
        _ = [stack.push(v) for v in self.list_ if v.indegree == 0]

        while not stack.is_empty():
            # print(stack)
            head = stack.peek()
            stack.pop()
            ret.append(head)

            node = head.link
            while node is not None:
                head = self[node.vertex]
                head.indegree -= 1
                if head.indegree == 0:
                    stack.push(head)
                node = node.link

        return ret

    def __getitem__(self, index):
        return self.list_[index]

    def __setitem__(self, index, value):
        self.list_[index] = value

    def __len__(self):
        return len(self.list_)

    def __str__(self):
        ret = ""

        for i, vt in enumerate(self):
            indegree = vt.indegree
            ret += f"v[{i}: {indegree}] = "
            if vt is None or vt.link is None:
                ret += str(None) + "\n"
                continue

            vt = vt.link
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret


if __name__ == "__main__":
    mat_ = read_input("input_aov_00.dat")
    print("Input matrix:")
    print_mat(mat_)

    print()
    print("Adjacency list:")
    list_ = GraphAovBuilder.build(mat_)
    graph = GraphAov(list_, mat_)
    print(graph)

    for i in range(len(graph)):
        print(f"v[{i}].outdegree = {graph.outdegree(i)}")
        print(f"v[{i}].indegree = {graph.indegree(i)}")

    print()
    print("Topology sorted:")
    topology = graph.sort_topology()
    print(topology)