# list, append()
# range() 함수와 append() 함수를 사용하여 리스트를 확장하는 예제 프로그램

L1 = list()
for n in range(10):
    L1.append(n)
print(L1)

L2 = list()
for n in range(1, 10, 2):
    L2.append(n)
print("L2 : ", L2)

L3 = list()
for n in range(0, 15, 3):
    L3.append(n)
print("L3 : ", L3)
#--==>>
'''
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L2 :  [1, 3, 5, 7, 9]
L3 :  [0, 3, 6, 9, 12]
'''