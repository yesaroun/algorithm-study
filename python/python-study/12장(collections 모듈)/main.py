from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)
#--==>> deque([0, 1, 2, 3, 4])

print(deque_list.pop())
print(deque_list.pop())
print(deque_list)
'''
4
3
deque([0, 1, 2])
'''