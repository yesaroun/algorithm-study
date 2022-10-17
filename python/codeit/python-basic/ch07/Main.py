
# 문제1
# i, hap = 0, 0
# num1, num2, num3 = 0, 0, 0
#
# num1 = int(input("시작값을 입력하세요 : "))
# num2 = int(input("끝값을 입력하세요 : "))
# num3 = int(input("증가값을 입력하세요 : "))
#
# i = num1
# while i <= num2:
#     hap = hap + i
#     i += num3
#
# print("%d에서 %d까지 %d씩 증가시킨 값의 합계 : %d" % (num1, num2, num3, hap))

# 문제2
# hap = 0
# a, b = 0, 0
#
# while True:
#     a = input("더할 첫 번째 수를 입력하세요 : ")
#     if a == "$":
#         break
#     else:
#         a = int(a)
#     b = int(input("더할 두 번째 수를 입력하세요 : "))
#     hap = a + b
#     print("%d + %d = %d" %(a, b, hap))
#
# print("$을 입력해 반복문을 탈출했습니다.")

# 문제3
# hap, i = 0, 0
#
# while i <= 100:
#     i += 1
#     hap += i
#
#     if hap >= 1000:
#         break
#
# print("1~100의 합계를 최초로 1000이 넘게 하는 숫자 : %d" %i)

# 문제4
i, k = 0, 0

i = 0
while i < 9:
    if i < 5:
        for k in range(4 - i):
            print('  ', end='')
        for k in range(i * 2 + 1):
            print('\u2605', end='')
        print()
    else:
        for k in range(i - 4):
            print('  ', end='')
        for k in range((i * 2) - ((i - 4) * 4 - 1)):
            print('\u2605', end='')
        print()

    i += 1