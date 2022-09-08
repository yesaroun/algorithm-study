num_bin = "1011"
print(f"binary number = {num_bin}")

exp = 0
num_dec = 0

cnt_iter = len(num_bin)     # 자릿수 확인
while cnt_iter > 0:         # 자릿수 만큼 돌기
    num_dec += 2**exp * int(num_bin[cnt_iter - 1])
    exp += 1
    cnt_iter -= 1

print(f"Decimal number = {num_dec}")