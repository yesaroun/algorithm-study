# mutable 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """mutable 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)

    for i in range(len(a) // 2):
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

if __name__ == "__main__":
    print("배열 원소를 역순으로 정렬")
    nx = int(input('원소 수 입력: '))
    # x = [None] * nx
    x = [None for _ in range(nx)]

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))

    reverse_array(x)

    print("배열 역순 정렬 완료")

    for i in range(nx):
        print(f'{x[i]}', end=" ")
