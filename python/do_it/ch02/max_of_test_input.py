# 배열 원소의 최댓값을 구해서 출력하기(원소값을 입력받음)

from max import max_of

print("배열의 최댓값을 구합니다.")
print("주의: 'End'를 입력하시면 종료합니다.")

number = 0
x = []      # 빈 래스트

while True:
    s = input(f'x[{number}]의 값 입력:' )
    if s == "End":
        break
    x.append(int(s))
    number += 1

print(f"{number}개를 입력")
print(f"최댓값 : {max_of(x)}")