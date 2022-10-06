# for-loop, break, continue
# 최대 100개의 정수를 입력받아 0이나 음수를 제외하고 합을 계산하는 프로그램이며
# 만약 -1이 입력되면 for-loop 중지

MAX_NUM_DATA = 100
num_data = 0
data_sum = 0
print("Input (up to {}) integer data.".format(MAX_NUM_DATA))
for i in range(MAX_NUM_DATA):
    data = int(input("Data (-1 to finish) = "))
    num_data = num_data + 1
    if data == -1:
        break
    elif data <= 0:
        num_data -= 1
        continue
    else:
        data_sum = data_sum + data

print("Total {} data input, sum of positive data = {}".format(num_data - 1, data_sum))
#--==>>
'''
Input (up to 100) integer data.
Data (-1 to finish) = 23
Data (-1 to finish) = -ch12
Data (-1 to finish) = 32
Data (-1 to finish) = 43
Data (-1 to finish) = -1
Total 3 data input, sum of positive data = 98
'''