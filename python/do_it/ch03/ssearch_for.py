# for 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(for 문)"""
    # 내 풀이
    """
    result = None
    for i in range(len(a)):
        if a[i] == key:
            result = i
            return result

    if result is None:
        return -1
    """

    for i in range(len(a)):
        if a[i] == key:
            return i        # 검색 성공(인덱스를 반환)
    return -1               # 검색 실패(-1을 반환)

if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요.: "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'{i}번째 값: '))

    ky = int(input('key값을 입력 : '))

    result = seq_search(x, ky)

    if result == -1:
        print('값이 존재하지 않아')
    else:
        print('값 : ', result)


