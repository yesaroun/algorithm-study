# 주어진 배열에서 어떤 부분 집합의 합이 특정 값인지 찾기


def isSubsetSum(arr: list[int], target: int) -> bool:
    arr_len = len(arr)
    for x in range(0, arr_len):
        for y in range(x, arr_len):
            if arr[x] + arr[y] == target:
                return True
    return False


arr = [3, 34, 4, 12, 5, 2]
target = 9
print(isSubsetSum(arr, target))
