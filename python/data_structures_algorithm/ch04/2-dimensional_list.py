# nested for_loop for 2-dimensional lists' addition and subtraction

A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,0,0], [0,1,0], [0,0,1]]
C = [[0,0,0], [0,0,0], [0,0,0]]
D = [[0,0,0], [0,0,0], [0,0,0]]

print("A : ", A)
print("B : ", B)
print()

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]
print("A+B => ", C)
print()

for i in range(3):
    for j in range(3):
        D[i][j] = A[i][j] - B[i][j]
print("A-B => ", D)
#--==>>
'''
A :  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B :  [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

A+B =>  [[2, 2, 3], [4, 6, 6], [7, 8, 10]]

A-B =>  [[0, 2, 3], [4, 4, 6], [7, 8, 8]]
'''