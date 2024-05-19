# 1,000 이하의 소수를 나열하기

counter = 0     # 나눗셈 회수를 카운트

for i in range(2, 1001):
    for j in range(2, i):
        counter += 1
        if i % j == 0:
            break
    else:
        print(i)
print(f'나눗셈을 실행한 횟수: {counter}')