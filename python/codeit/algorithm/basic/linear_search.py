# 내 답
# def linear_search(element, some_list):
#     result = None
#     num = 0
#
#     while num < len(some_list):
#         if some_list[num] == element:
#             result = num
#         num += 1
#
#     return result

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))