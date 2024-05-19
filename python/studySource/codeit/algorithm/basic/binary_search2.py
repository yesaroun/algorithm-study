import math


def binary_search(element, some_list):
    list_len = len(some_list)
    if list_len == 0:
        return None

    current_idx = math.ceil((list_len-1) / 2)
    if element == some_list[current_idx]:
        return current_idx
    elif element > some_list[current_idx]:
        new_list = some_list[current_idx+1:]
        return binary_search(element, new_list)
    else:   # element < some_list[current_idx]
        return binary_search(element, some_list[:current_idx])


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
