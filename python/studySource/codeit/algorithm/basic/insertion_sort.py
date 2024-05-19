# 1. 리스트의 두 번째 항목에서 시작하여 왼쪽의 항목과 비교합니다.
# 2. 현재 항목이 왼쪽 항목보다 작으면 왼쪽 항목을 오른쪽으로 이동시킵니다.
# 3. 이를 현재 항목이 왼쪽 항목보다 크거나 왼쪽에 더 이상 항목이 없을 때까지 반복합니다.
# 4. 그런 다음 현재 항목을 마지막으로 비어 있는 위치에 삽입합니다.
# 5. 이 과정을 리스트의 모든 항목에 대해 반복합니다.


def insertion_sort2(arr: list[int]) -> list[int]:
    length: int = len(arr)
    # 배열 전체를 반복하면서
    for index_1 in range(1, length):
        for index_2 in range(index_1 - 1, -1, -1):
            if arr[index_2 + 1] < arr[index_2]:
                arr[index_2 + 1], arr[index_2] = arr[index_2], arr[index_2 + 1]
            else:
                break
    return arr


def insertion_sort(arr: list[int]) -> list[int]:
    # 배열 전체를 반복하면서
    for i in range(1, len(arr)):
        key: int = arr[i]

        # 이미 정렬된 배열 부분에서 올바른 위치를 찾아가는 과정
        j: int = i - 1
        while j >=0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    arr: list[int] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(insertion_sort(arr))
    # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
