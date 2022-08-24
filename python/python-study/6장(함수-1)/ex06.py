# 간단한 사칙연산 계산기 만들기

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return round((x / y), 2)




temp = "y"

# 연산자에 의해서 분기를 시킨다.
while True:
    if temp == "n":
        break
    elif temp == "y":
        num1 = float(input("첫 번째 수 입력 : "))
        num2 = float(input("두 번째 수 입력 : "))
        op = input("원하는 연산을 입력(+, -, *, /) : ")
        if op == "+":
            print("n1 + n2 = ", add(num1, num2))
        elif op == "-":
            print("n1 - n2 = ", substract(num1, num2))
        elif op == "*":
            print("n1 * n2 = ", multiply(num1, num2))
        elif op == "/":
            print("n1 / n2 = ", divide(num1, num2))
        else:
            print("잘못된 연산자입니다.")
        temp = input("계산을 계속 하시겠습니까?(y or n) ")
    else:
        print("제대로된 종료문자를 입력해주세요.")
        break