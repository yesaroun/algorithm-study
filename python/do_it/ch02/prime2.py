# 1,000 이하의 소수를 나열하기(알고리즘 개선1)

counter = 0     # 나눗셈 횟수를 카운트
ptr = 0         # 이미 찾은 소수의 개수
prime = [None for _ in range(501)]  # 소수를 저장하는 배열

prime[0] = 2

for i in range(3, 1001, 2):
    for j in range(ptr):
        counter += 1
        if i % prime[j] == 0:
            break
    else:
        ptr += 1
        prime[ptr] = i


for i in range(ptr):        # ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')