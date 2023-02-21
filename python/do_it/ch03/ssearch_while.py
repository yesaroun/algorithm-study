# while 문으로 작성한 선형 검색 알고리즘
# 선형 검색 : 직선 모양으로 늘어선 배열에서 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하는 검색 알고리즘. 

from typing import Any, Sequence 


def seq_search(a: Sequence, key: Any) -> int:
    """sequence a에서 key와 값이 같은 원소를 선형 검색(while문)"""
    i = 0

    while True:
        if len(a) == i:
            return -1
        if a[i] == key:
            return i
        i += 1


if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요: "))
    arrs = [None] * num
    
    for arr_num in range(num):
        arrs_num = int(input(f'{arr_num} 번째 값: '))
        arrs[arr_num] = arrs_num 

    ky = int(input("검색할 값을 입력하세요: "))

    idx = seq_search(arrs, ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print("검색한 요소 위치 : ", idx)





