# 사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하여 반환하는
# 함수 decTobin(num)를 작성하고 테스트 해보시오.

def decTobin(num):
    binary = ""

    while num != 0:
        value = num % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = num // 2
        print("num : ", num)
    return binary

decNum = int(input("10진수를 입력하세요 : "))
print("10진수 {}를 2진수로 변경한 값 : {}".format(decNum, decTobin(decNum)))
#--==>>
'''
10진수를 입력하세요 : 321
num :  160
num :  80
num :  40
num :  20
num :  10
num :  5
num :  2
num :  1
num :  0
10진수 321를 2진수로 변경한 값 : 101000001
'''