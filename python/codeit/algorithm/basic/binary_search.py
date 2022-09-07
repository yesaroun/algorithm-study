def binary_search(element, some_list):
    bool_result = True      # 반복문을 끝내기 위한 변수
    result = None           # 결과값을 저장할 변수
    copy_some_list = some_list

    while bool_result:
        result = len(some_list) // 2
        if element == result:
            bool_result = False
        elif element > some_list[result]:


    return result


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))