# 1 부터 n까지의 정수의 합 구하기(n은 양수만 입력받음)

print('1~n 까지 정수의 합을 구합니다.')

while True:
    n = int(input("정수 입력: "))
    if n>0:
        break

sum = 0

for i in range(1, n+1):
    sum += i
    i += 1

print(f'1~{n}까지 정수의 합은 {sum}입니다.')