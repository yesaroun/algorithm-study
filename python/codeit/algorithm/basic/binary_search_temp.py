def binary_search(element, some_list):
    start_idx = 0
    end_idx = len(some_list) - 1

    while True:
        if end_idx <= start_idx:
            return None

        if start_idx == 0:
            current_idx = (end_idx - start_idx) // 2
        else:
            current_idx = (end_idx - start_idx) // 2 + start_idx

        if element == some_list[current_idx]:
            return current_idx
        elif element > some_list[current_idx]:
            start_idx = current_idx
        else:  # element < some_list[current_idx]
            end_idx = current_idx


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
