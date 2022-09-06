num_bin = "1011"
print(f"binary number = {num_bin}")

num_dec = 0

num_bin = num_bin[::-1]

cnt_iter = 0
while cnt_iter < len(num_bin):
    num_dec += 2**cnt_iter * int(num_bin[cnt_iter])
    cnt_iter += 1

print(f"Decimal number = {num_dec}")