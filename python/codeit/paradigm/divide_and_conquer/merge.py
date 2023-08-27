# `merge` 함수는 정렬된 두 리스트 `list1`과 `list2`를 받아서, 하나의 정렬된 리스트를 리턴합니다.
# 내 풀이

def merge(list1: list[int], list2: list[int]) -> list[int]:
    result_list: list = []
    list1_index: int = 0
    list2_index: int = 0
    list1_len: int = len(list1)
    list2_len: int = len(list2)

    checker: bool = True
    while checker:
        if list1 == [] and list2 == []:
            checker = False
        elif not list1 or list1_index >= list1_len:
            for index in range(list2_index, list2_len):
                result_list.append(list2[index])
            checker = False
        elif not list2 or list2_index >= list2_len:
            for index in range(list1_index, list1_len):
                result_list.append(list1[index])
            checker = False
        else:
            if list1[list1_index] < list2[list2_index]:
                result_list.append(list1[list1_index])
                list1_index += 1
            else:
                result_list.append(list2[list2_index])
                list2_index += 1

    return result_list


# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))