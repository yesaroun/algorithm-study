class Node:
    def __init__(self, item=None):
        self.item = item
        self.link = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        if self is other or self.item == other.item:
            return True

        return False

    def __str__(self):
        return f"{self.item}"

class UndiGraph:
    def __init__(self, mat):
        self.mat = mat
        self.vertices = len(mat)
        self.linked = [None] * self.vertices
        self.__build()

    def __build(self):
        size = len(mat)
        for row in range(size):
            for col in range(size):
                if not self.mat[row][col]:
                    continue
                self.add_edge(row, col)

    def add_edge(self, src, dst):
        if self.linked[src] is None:
            self.linked[src] = Node(dst)
            return

        # already exist
        prev = vt = self.linked[src]
        while vt is not None:
            prev, vt = vt, vt.link

        prev.link = Node(dst)

    def __str__(self):
        ret = ""
        for i, vt in enumerate(self.linked):
            ret += f"v[{i}] = "
            if vt is None:
                ret += "None\n"
                continue
            while vt is not None:
                ret += f"{vt}, "
                vt = vt.link
            ret += "\b\b \n"
        return ret

def read_input(name_file="input.dat"):
    mat = []
    with open(name_file) as f:
        for line in f:
            (*row,) = map(int, line.split())
            mat.append(row)
    return mat

def print_mat(mat):
    rows, cols = len(mat), len(mat[0])
    print("Input matrix")
    for row in range(rows):
        for col in range(cols):
            print(f"{mat[row][col]}", end=" ")
        print("\b")

if __name__ == "__main__":
    mat = read_input("input_g4.dat")
    print_mat(mat)

    print()
    print("Adjacency list")
    graph = UndiGraph(mat)
    print(graph)