# ternary selection statements to find max and min

x, y = map(int, input('input two integers (x, y): ').split())

Max = x if x > y else y
Min = x if x < y else y

print("Input data (%d, %d) => max (%d), min(%d)"%(x, y, Max, Min))
#--==>>
'''
input two integers (x, y): 3 4
Input data (3, 4) => max (4), min(3)
'''