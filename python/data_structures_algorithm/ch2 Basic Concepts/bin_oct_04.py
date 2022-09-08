num_bin = "1011"
print(f"Binary number = {num_bin}")

BIT = 3
num_bin = num_bin[::-1]
num_oct = []

# 순환을 2번 하면 되는데 가장 큰 로직은 전체 사이즈 만큼 돌리기
# 자료구조 하는 동안 for문은 거의 쓰지 않을 것이다.
# 왜냐하면 while문을 빨리 생각하는게 편하다.

cnt_bit = 0
while cnt_bit < len(num_bin):
    cnt, sum_ = 0, 0

    while cnt < BIT:
        if cnt_bit >= len(num_bin):
            break

        sum_ += 2**cnt * int(num_bin[cnt_bit])
        cnt += 1
        cnt_bit += 1

    num_oct.append(sum_)

num_oct = num_oct[::-1]
num_oct = "".join(map(str, num_oct))
print(f"Octal number = {num_oct}")