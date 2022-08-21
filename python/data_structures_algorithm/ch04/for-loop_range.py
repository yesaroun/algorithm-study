# for-loop with range()
L = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
n = len(L)
L_sum = 0

print("L = ", L)
print("len(L) = ", len(L))

for i in range(n):          # L_sum = sum(range(0, n+1))
    d = L[i]
    L_sum += d
    print("L[%2d] = %2d" %(i, d))
print("L_sum = {}, avg = {}".format(L_sum, L_sum/len(L)))
#--==>>
'''
L =  [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
len(L) =  10
L[ 0] =  1
L[ 1] =  3
L[ 2] =  5
L[ 3] =  7
L[ 4] =  9
L[ 5] =  2
L[ 6] =  4
L[ 7] =  6
L[ 8] =  8
L[ 9] = 10
L_sum = 55, avg = 5.5
'''