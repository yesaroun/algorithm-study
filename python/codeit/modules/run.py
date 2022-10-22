from area import circle, square

# 이 상황에서 또 다른 square 함수 정의

def square(length):
    return 4 * length

print(dir())
print(square(3))
# 현재 파일에 있는 square함수를 정의한다
# 파이썬에서는 똑같은 이름으로 여러 함수가 정의되었을 때
# 가장 나중에 정의된 함수를 쓴다
# 하지만 지금처럼 이름이 중복되면 바람직하지 않다
# 그래서 한 네임스페이스 안에는 같은 이름이 중복되지 않는게 좋다.
# 중복되지 않게 하는 첫 번째 방법은 square 함수를 가져올 때 이름을 바꿔 주는 것이다.
# from area import square as sq
# 다른 방법은 모듈 그대로 import 하는 방법이다.
# import area