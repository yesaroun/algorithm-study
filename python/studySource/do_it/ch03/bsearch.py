# 이진 검색 알고리즘

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0                  # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1         # 검색 범위 맨 끝 원소의 인덱스
    result: int
    
    while True:
        pc = (pl + pr) // 2     # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc           # 검색 성공
        elif a[pc] < key:
            pl = pc + 1         # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1         # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    return -1

    """내 풀이
        if pl >= pr:
            result = -1
            break

        divied_num = (pr + pl) // 2  
        
        if a[divied_num] == key:
            result = divied_num
            break
        
        if a[divied_num] > key:
            pr = divied_num 
        else:
            pl = divied_num  

    return result
    """


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num        # 원소 수가 num인 배열을 생성

    print('배열을 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))
    
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:            # 바로 직전에 입력한 원솟값보다 큰 값을 입력 
                break

    ky = int(input('검색할 값 입력: '))     # 검색할 키값 ky를 입력

    idx = bin_search(x, ky)                 # ky값과 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'겂색값은 x[{idx}]에 있습니다.')


