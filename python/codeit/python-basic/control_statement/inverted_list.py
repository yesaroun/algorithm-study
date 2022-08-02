numbers = [2, 3, 5, 7, 11, 13, 17, 19]

'''
5
0 1 2 3 4
5-5 5-4 ... 5-1
'''

# 리스트 뒤집기
def list_inverter(list):
    temp = []
    for i in range(1, len(list) + 1):
        temp.append(list[len(list) - i])

    for i in range(len(list)):
        list[i] = temp[i]

list_inverter(numbers)

'''
temp = []

for i in range(1, len(numbers) + 1):
    temp.append(numbers[len(numbers) - i])

for i in range(len(numbers)):
    numbers[i] = temp[i]
'''

print("뒤집어진 리스트: " + str(numbers))
#--==>> 뒤집어진 리스트: [19, 17, 13, 11, 7, 5, 3, 2]