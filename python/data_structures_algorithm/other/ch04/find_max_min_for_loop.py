#for_looop to find max and min

n = int(input("Input the number of data to process: "))
print("Input %d integers"%(n))
count = 0
d = int(input("1 : "))
Max = Min = d

for i in range(n-1):
    d = int(input("{} : ".format(i + 2)))
    if d > Max:
        Max = d
    if d < Min:
        Min = d

print("Max : ", Max)
print("Min : ", Min)

#--==>>
'''
Input the number of data to process: 5
Input 5 integers
1 : 2
2 : 23
3 : 21
4 : 54
5 : 23
Max :  54
Min :  2
'''