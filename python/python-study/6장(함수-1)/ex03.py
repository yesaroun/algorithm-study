# 두개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서 큰 수를 리턴하는
# 함수를 만들어보자.

# 함수의 목록이 정의되어 있는 모듈을 import할 때는 항상 개발코드의 상위에
# 위치할 수 있도록 해야 한다.
from calc import *

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
value = get_max(num1, num2)

print("{}과 {}의 값 중에 큰 값은 {}이다.".format(num1, num2, value))
#--==>>
'''
num1 : 100
num2 : 800
100과 800의 값 중에 큰 값은 800이다.
'''

# 거듭제곱을 구하는 코드
num1 = int(input("거듭 제곱 대상 숫자 : "))
num2 = int(input("거듭 제곱 횟수 : "))
value = power(num1, num2)

print("{}과 {}의 거듭제곱 값은 {}이다.".format(num1, num2, value))
#--==>>
'''
거듭 제곱 대상 숫자 : 2
거듭 제곱 횟수 : 4
2과 4의 거듭제곱 값은 16이다.
'''