import math

sum = 0

# 양의 정수를 입력받기 위한 예외처리
while True:
    num = int(input("양의 정수 입력 : "))
    if num <= 0:
        print("올바른 수를 다시 입력하세요.")
    else:
        break

# num을 문자열로 변환하는 방식
# num = str(num)
#
# for i in range(len(num)):
#     sum += int(num[i])

# 변수 cnt_iter 을 exp로 바꾸기
cnt_iter = int(math.log(num, 10))
count = 0

# 이 방식 집에서 다시 봐보기!
# while cnt_iter > 0:
#     sum, num = sum + num // (10 ** cnt_iter), num - (num // (10 ** cnt_iter) * (10 ** cnt_iter) )
#     cnt_iter -= 1
#     count += 1
#
# sum = sum + num

# 두번째 파라미터가 -1인 이유는 0까지 불러와야 하기 때문이다.
for i in range(cnt_iter, -1, -1):
    x = num // (10 ** i)
    sum += x
    num -= x * (10 ** i)

print(f"입력 받은 양의 정수의 각 자리수 합은 {sum}입니다.")