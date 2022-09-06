# embedded functions for nubmer data
x = -123
print("x     = {:4d}".format(x))
print("abs(x)= {:4d}".format(abs(x)))

a, b = 7, 2
print("a = ", a)
print("b = ", b)

q, r = divmod(a, b)
print("q, r = divmod(a, b)")
print("q = ", q)
print("r = ", r)

a_b = pow(a, b)
print("pow({}, {}) = {}".format(a, b, a_b))

c = 3.1415926535
c_r = round(c, 4)
print("c = ", c)
print("c_r = ", c_r)
#--==>>
'''
x     = -123
abs(x)=  123
a =  7
b =  2
q, r = divmod(a, b)
q =  3
r =  1
pow(7, 2) = 49
c =  3.1415926535
c_r =  3.1416
'''