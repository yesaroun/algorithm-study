def selection_sort(arr: list[int]) -> list[int]:
    length: int = len(arr)
    # 배열 전체를 반복하면서
    for index_1 in range(length):
        min_index: int = index_1
        # 현재 위치에서 가장 작은 원소를 찾습니다.
        for index_2 in range(index_1 + 1, length):
            if arr[min_index] > arr[index_2]:
                min_index = index_2

        # 가장 작은 원소와 현재 원소를 교환합니다.
        arr[index_1], arr[min_index] = arr[min_index], arr[index_1]

    return arr


if __name__ == "__main__":
    arr: list[int] = [3, 1, 4, 9, 5, 7, 5]
    print(selection_sort(arr))
