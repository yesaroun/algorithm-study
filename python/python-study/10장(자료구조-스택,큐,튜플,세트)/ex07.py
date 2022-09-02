# 문제 : 원의 넓이와 둘레를 동시에 반환하는 함수를 작성하고 테스트 하라
# 반지름은 사용자로부터 입력을 받는다.
# 출력결과
# 원의 반지름을 입력하시오: 10
# 원의 넓이는 314.1592   이고 원의 둘레는 62.8318   이다.
import math

def calcCircle(radius):
    # 원의 넓이
    area = radius * radius * math.pi
    # 원의 둘레
    circumstance = radius * 2 * math.pi
    # 값을 다중으로 넘기고 싶을 때 튜플을 사용하면 된다.
    return (area, circumstance)

if __name__ == "__main__":
    radius = float(input("원의 반지름을 입력하세요 : "))
    # 함수의 리턴타입이 튜플이니 저장하기 위해서는 튜풀로 반환값을 저장하고 있다.
    (area, circumstance) = calcCircle(radius)
    print("원의 넓이는", area, "이고 원의 둘레는", circumstance, "이다.")
