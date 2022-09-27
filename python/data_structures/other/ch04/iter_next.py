# for-loop with range()

L = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
n = len(L)
it = iter(L)

for i in range(n):      #sSum = sum(range(0, n+1))
    d = next(it)
    print("L[%2d] = %2d" %(i, d))

#--==>>
'''
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
'''