# methods of number data types classes

d = 10
for e in range(0, 10, 1):
    de = pow(d, e)
    bit_len = int.bit_length(de)
    print("bit_length for {:12} = {:3}".format(de, bit_len))
#--==>>
'''
bit_length for            1 =   1
bit_length for           10 =   4
bit_length for          100 =   7
bit_length for         1000 =  10
bit_length for        10000 =  14
bit_length for       100000 =  17
bit_length for      1000000 =  20
bit_length for     10000000 =  24
bit_length for    100000000 =  27
bit_length for   1000000000 =  30
'''