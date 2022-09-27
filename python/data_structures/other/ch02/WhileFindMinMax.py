# whie-loop, find min and max of input data list
# 지정된 개수의 데이터를 입력받으며 최댓값과 쵀솟값을 찾는 프로그램

TARGET_NUM_DATA = 10
INT_MAX = 2147483647
INT_MIN = -2147483638
num_data = 0
data_min = INT_MAX
data_max = INT_MIN
L_data = [] # empty list

print("Input {} integer data.".format(TARGET_NUM_DATA))
while num_data < TARGET_NUM_DATA:
    data = int(input("data = "))
    num_data = num_data + 1
    L_data.append(data)

    if data < data_min:
        data_min = data
    elif data > data_max:
        data_max = data
    else:
        continue

print("Input data list = ", L_data)
print("Min = {}, Max = {}".format(data_min, data_max))
#--==>>
'''
Input 10 integer data.
data = 39
data = 23
data = 43
data = 54
data = 63
data = 24
data = 54
data = 65
data = -5
data = -43
Input data list =  [39, 23, 43, 54, 63, 24, 54, 65, -5, -43]
Min = -43, Max = 65
'''