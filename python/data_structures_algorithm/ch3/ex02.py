
sum_ = 0

# 양의 정수를 입력받기 위한 예외처리
while True:
    num = int(input("양의 정수 입력 : "))
    if num <= 0:
        print("올바른 수를 다시 입력하세요.")
    else:
        break

exp = int(math.log(num, 10))
count = 0

while num != 0:
    sum_ = sum_ + num % 10
    num = num // 10

print(f"입력 받은 양의 정수의 각 자리수 합은 {sum_}입니다.")