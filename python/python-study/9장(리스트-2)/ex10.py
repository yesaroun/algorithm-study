# 정렬하기에 대한 실습
list1 = [4, 8, 9, -1, 10]
# 리스트 객체에서 제공해주는 sort()를 이용하여 정렬하는 방법
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
'''
[-1, 4, 8, 9, 10]
[10, 9, 8, 4, -1]
'''

# 선택 정렬 알고리즘을 통한 정렬하기
# 선택 정렬이라는 주어진 리스트 중에서 일단 최솟괎을 찾는다.
# 그 최솟값을 맨 앞에 위치한 값과 교환한다.
# 맨 처음 위치를 뺀 나머지 리스트를 위와 똑같은 방법으로 루핑하면서
# 최종적으로 정렬이 이루어진다.
# 선태 정렬은 제자리 정렬이기 때문에 더블루프를 사용해야 한다.
def selectionSort(li):
    cnt = 0
    for i in range(len(li) - 1):
        min_idx  = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j