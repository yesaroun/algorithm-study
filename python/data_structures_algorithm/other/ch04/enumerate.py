# for-loop with enumerate()
L = [10, 30, 50, 70, 90, 20, 40, 60, 80, 100]

# part 1
for item in enumerate(L):
    # print("type(item) : ", type(item))
    # print(item)
    print("L[{:2}] = {:4}".format(item[0], item[1]))
print()

# part 2
for i, value in enumerate(L):
    print("L[{:2}] = {:4}".format(i, value))

print()

# part 3
for item in enumerate(L, 100):
    print("item[0] = {:4}, item[1] = {:4}".format(item[0], item[1]))

#--==>>
'''
L[ 0] =   10
L[ 1] =   30
L[ 2] =   50
L[ 3] =   70
L[ 4] =   90
L[ 5] =   20
L[ 6] =   40
L[ 7] =   60
L[ 8] =   80
L[ 9] =  100

L[ 0] =   10
L[ 1] =   30
L[ 2] =   50
L[ 3] =   70
L[ 4] =   90
L[ 5] =   20
L[ 6] =   40
L[ 7] =   60
L[ 8] =   80
L[ 9] =  100

item[0] =  100, item[1] =   10
item[0] =  101, item[1] =   30
item[0] =  102, item[1] =   50
item[0] =  103, item[1] =   70
item[0] =  104, item[1] =   90
item[0] =  105, item[1] =   20
item[0] =  106, item[1] =   40
item[0] =  107, item[1] =   60
item[0] =  108, item[1] =   80
item[0] =  109, item[1] =  100
'''