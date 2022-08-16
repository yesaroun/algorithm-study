# for-loop with range()
n = int(input('input n to calculate sum of [0..n] : '))
nSum = 0

for i in range(0, n+1):     #sSum = sum(range(0, n+1))
    nSum += i

print("Sum of [0..%d] = %d" %(n, nSum))