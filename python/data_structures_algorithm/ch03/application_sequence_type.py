# Application of sequence type

L = [4, 5, 6, 1, 3, 8, 9, 2, 0, 7]
sum_L = sum(L)
max_L = max(L)
min_L = min(L)
len_L = len(L)
avg_L = sum_L / len_L
print("L (size: {}) : {}".format(len_L, L))
print("Statistics of L : Max ({}), Min ({}), Avg({:7.2f})".format(max_L, min_L, avg_L))

L_sorted = sorted(L)
print("Sorted L : ", L_sorted)
print("Original L : ", L)
#--==>>
'''
L (size: 10) : [4, 5, 6, 1, 3, 8, 9, 2, 0, 7]
Statistics of L : Max (9), Min (0), Avg(   4.50)
Sorted L :  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Original L :  [4, 5, 6, 1, 3, 8, 9, 2, 0, 7]
'''