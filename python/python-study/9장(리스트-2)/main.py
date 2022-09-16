def func2(list):
    list[0] = 99

values = [0, 1, 2, 3]
print(values)
func2(values)
print(values)
'''
[0, 1, 2, 3]
[99, 1, 2, 3]
'''