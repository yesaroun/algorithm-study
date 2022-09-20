def transpose_mat(self):


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
print("transpose >>")
mat = mat.transpose()
print(mat)