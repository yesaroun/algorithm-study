# while-loop
# 리스트를 생성하고 while-loop를 사용하여 반복적으로 정수를 입력받아 리스트에 추가한 후 sum에 합산
# 입력 데이터 값이 음수이면 while-loop가 종료된다.

L = list()
print("Input integers (-1 to end)")
x = int(input("data : "))
n = 0
sum = 0
while x >= 0:
    L.append(x)
    n += 1
    sum += x
    x = int(input("data : "))

print("Total ", n, " integers were input: ", L)
print("Sum is : ", sum)
#--==>>
'''
Input integers (-1 to end)
data : 34
data : 23
data : 3
data : -1
Total  3  integers were input:  [34, 23, 3]
Sum is :  60
'''