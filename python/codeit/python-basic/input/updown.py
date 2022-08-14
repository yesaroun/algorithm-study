import random

rand_num = random.randint(1, 20)
ans = 0

for i in range(1, 5):
    ans = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(i)))

    if ans == rand_num:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(i))
        break
    elif ans > rand_num:
        print("down")
    elif ans < rand_num:
        print("up")

if ans != rand_num:
    print("아쉽습니다. 정답은 {}였습니다.".format(rand_num))



