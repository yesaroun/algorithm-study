# while-loop, break, continue
# while문으로 최대 100개의 정수 데이터를 입력하며 입력된 데이터를 data_sum으로 합산하여 결과를 출력

MAX_NUM_DATA = 100
num_data = 0
data_sum = 0
print("Input (up to {} ) integer data.".format(MAX_NUM_DATA))
while num_data < MAX_NUM_DATA:
    data = int(input("Data (-1 to finish) = "))
    num_data = num_data + 1
    if data == -1:
        break
    elif data <= 0:
        continue
    else:
        data_sum = data_sum + data

print("Total {} data input, sum of positive data = {}".format(num_data, data_sum))
#--==>>
'''
Input (up to 100 ) integer data.
Data (-1 to finish) = 34
Data (-1 to finish) = 23
Data (-1 to finish) = 43
Data (-1 to finish) = -1
Total 4 data input, sum of positive data = 100
'''