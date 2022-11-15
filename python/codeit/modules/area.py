print("area 모듈 이름: {}".format(__name__))
#--==>>area 모듈 이름: __main__

PI = 3.14

def circle(radius):
    return PI * radius * radius

def square(length):
    return length * length

# __name__ : 모듈의 이름을 저장해 놓은 변수이다.
# __name__의 값은 파이썬이 알아서 정해준다.
# 만약 파이썬 파일을 직접 실행하면
# 그 파일의 __name__은 main으로 설정되고
# 파일을 다른 곳에서 import해서 설정하면 name은 원래 모듈 이름(지금은 area)으로 설정된다.

if __name__ == "__main__":
    print(circle(2) == 12.56)
    print(square(2) == 4)
"""
True
True
"""
# 이렇게 하면 run.py에서 조건문이 충족되지 않으므로 출력되지 않는다.