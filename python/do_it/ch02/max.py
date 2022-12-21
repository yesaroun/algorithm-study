# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값을 반환"""
    max_num = a[0]
    for i in range(1, len(a)):
        if a[i] > max_num:
            max_num = a[i]

    return max_num

if __name__ == "__main__":
    print("배열의 최댓값을 구합니다.")
    num = int(input("원소 수 입력: "))
    x = [None for _ in range(num)]  # 원소의 수가 num인 리스트를 생성
    # x = [None] * num

    for i in range(num):
        x[i] = int(input("수 입력: "))

    print(f'최댓값 : {max_of(x)}')