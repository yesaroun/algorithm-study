# indexing of str data type

S = "0123456789ABCDEFG"
print("S (type: {}, len: {})= {}".format(type(S), len(S), S))

for i in range(len(S)):
    print("S[{:2}] = {:2}".format(i, S[i]), end='  ')
    if i % 5 == 0:
        print()

print("\nS[0] = {}, S[-1] = {}".format(S[0], S[-1]))
S[0] = "X"
#--==>>
'''
S (type: <class 'str'>, len: 17)= 0123456789ABCDEFG
S[ 0] = 0   
S[ 1] = 1   S[ 2] = 2   S[ 3] = 3   S[ 4] = 4   S[ 5] = 5   
S[ 6] = 6   S[ 7] = 7   S[ 8] = 8   S[ 9] = 9   S[10] = A   
S[11] = B   S[12] = C   S[13] = D   S[14] = E   S[15] = F   
S[16] = G   
S[0] = 0, S[-1] = G
Traceback (most recent call last):
  File "/Users/akor1/Documents/programing/code/algorithm/python/data_structures/ch03/indexing_str_data.py", line 12, in <module>
    S[0] = "X"
TypeError: 'str' object does not support item assignment
'''