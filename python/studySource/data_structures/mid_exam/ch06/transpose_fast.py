class Term:
    def __init__(self, row=0, col=0, value=0):
        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return f"{self.row, self.col, self.value}"

    def __repr__(self):
        return str(self)

class MatrixSparse:
    def __init__(
            self, rows=0, cols=0, size=0, sparse = None
    ):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.sparse = sparse

    def build_matrix_sparse(self, mat):
        self.rows = len(mat)
        self.cols = len(mat[0])

        # sparse 행렬 생성
        self.sparse = [
            Term(r, c, v)
            for r, row in enumerate(mat)
            for c, v in enumerate(row)
            if v != 0
        ]
        self.size = len(self.sparse)

    def __str__(self):
        return f"{self.sparse}"

    def transpose(self):
        if self.sparse is None:
            return

        sparse = [Term() for _ in range(self.size)]

        row_term = []
        starting_num = []

        # 초기화
        for _ in range(self.cols):
            row_term.append(0)
            starting_num.append(0)

        # 각 열의 원소 수를 계산
        for i in range(len(self.sparse)):
            row_term[self.sparse[i].col] = row_term[self.sparse[i].col] + 1

        # 시작 위치 계산
        starting_num[0] = 1
        for i in range(1, self.cols):
            starting_num[i] = (starting_num[i-1] + row_term[i-1])

        # 시작 위치를 이용해서 특정 원소의 저장위치 파악
        for i in range(len(self.sparse)):
            # j = starting_num[self.sparse[i].col] = starting_num[self.sparse[i].col] + 1
            j = starting_num[self.sparse[i].col] + 1
            # print(j)
            # print(sparse)
            # print(self.sparse[i].col, self.sparse[i].row, self.sparse[i].value)
            sparse[i].row = self.sparse[i].col
            sparse[i].col = self.sparse[i].row
            sparse[i].value = self.sparse[i].value

        return MatrixSparse(
            rows=self.cols,
            cols=self.rows,
            size=self.size,
            sparse=sparse,
        )


data = [
    [15, 0, 0, 22, 0, -15],
    [0, 11, 3, 0, 0, 0],
    [0, 0, 0, -6, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [91, 0, 0, 0, 0, 0],
    [0, 0, 28, 0, 0, 0],
]

print("sparse matrix >>")
mat = MatrixSparse()
mat.build_matrix_sparse(data)
print(mat)


print("-" * 30)
# 13 추가
print("transpose >> ")
mat = mat.transpose()
print(mat)