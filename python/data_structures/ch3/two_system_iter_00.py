import math

BASE = 2    # 2 진수
num_dec = 11    # 입력되는 10진수
print(f"Decimal number = {num_dec}")    # 입력 10진수 출력

num_bin = ""   # 출력을 위한 공백 문자열을 준비

# 내 방식
# cnt_iter = 0
# tmp_num_dec = num_dec
#
# while tmp_num_dec > 1:
#     tmp_num_dec = tmp_num_dec // BASE
#     cnt_iter += 1

# log 사용한 방식
cnt_iter = int(math.log(num_dec, 2))

for _ in range(cnt_iter):
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin

# 마지막 나눗셈의 몫을 연결
if num_dec == 1:
    num_bin = str(num_dec) + num_bin

# 최종 계산된 2진수를 출력
print(f"Binary number = {num_bin}")