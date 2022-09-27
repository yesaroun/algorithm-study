# while-loop, find min and max of input data list
# 리스트에 포함되는 원소들을 input() 함수를 사용하여 입력 받아 설정하며
# 입력된 원소들의 최댓값과 최솟값 및 평균값을 계산하여 출력하는 예제

TARGET_NUM_DATA = 10
L = []  # empty list
num_data = 0

print("Input {} integer data.".format(TARGET_NUM_DATA))
while num_data < TARGET_NUM_DATA:
    data = int(input("data = "))
    L.append(data)
    num_data += 1

L_min = min(L)
L_max = max(L)
L_sum = sum(L)
L_len = len(L)

print("L (num_data = {}) = {}".format(L_len, L))
print("Min = {}, Max = {}, Avg = {}".format(L_min, L_max, L_sum / L_len))
#--==>>
'''
data = 7
data = 4
data = 2
data = 6
data = 4
data = 7
data = 4
data = 8
data = 4
data = 5
L (num_data = 10) = [7, 4, 2, 6, 4, 7, 4, 8, 4, 5]
Min = 2, Max = 8, Avg = 5.1
'''