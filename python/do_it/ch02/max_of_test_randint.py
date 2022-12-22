# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from max import max_of

print("난수의 최댓값을 구합니다")
num = int(input("난수 개수 입력: "))
lo = int(input("난수 최솟값 입력: "))
hi = int(input("난수 최댓값 입력: "))
x = [None for _ in range(num)]          # 원소 수가 num인 리스트를 생성
# print(x)

for i in range(num):
    x[i] = random.randint(lo, hi)       # lo 이상 hi 이하인 정수 난수 반환

print(f'{(x)}')
print(f'최댓값 : {max_of(x)}')
