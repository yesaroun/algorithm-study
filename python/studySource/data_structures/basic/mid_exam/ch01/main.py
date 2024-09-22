# 파이썬 -> 인터프리터 언어 고급언어

# 변수를 사용하는 이유는 기억장치(메모리)의 효율적인 사용
# 변수는 사용하기 전에 반드시 할당되어 있어야 한다

# 식별자 : 변수, 객체, 함수, 클래스, 모듈에 구분 혹은 식별하기 위해 프로그래머가 붙이는 이름
# 식별자 명명 규칙
"""
- 영문의 경우 대소문자 구분
- 식별자의 첫 글자는 숫자 불가
- 예약어 사용 불가
- '_'이외 특수문자, 문장부호, 공백문자 사용 불가
- 식별자의 길이 제한 없음

스네이크 케이스 : _을 사용하여 구분, 주로 변수와 함수의 이름에 활용
케멀 케이스 : 단어의 첫 글자마다 영문 대문자를 사용, 주로 클래스의 이름 지정
"""

# 예약어 : 파이썬에서 이미 문법적인 용도로 사용되고 있기에, 변수명 등의 식별자로 사용하면 안되는 단어들
# 예약어를 변수에 활용할 경우 오류는 발생하지 않으나, 예약어의 고유 기능이 사라진다
dir = 2
print(dir)
#--==>> 2

# 파이썬의 키워드를 변수에 활용할 경우 오류 발생
# 파이썬의 키워드
import keyword
print(keyword.kwlist)
#--==>> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class_', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 2진수, 8진수, 16진수도 정수형으로 분류

# 파이썬 3 버전에서는 정수나눗셈 연산자(//)와 실수나눗셈 연산자(/)가 구분된다.

# 일부 문자열만 정수형, 실수형(float), 복소수형(complex)으로 변환가능

# bool(정수형, 실수형, 복소수, 문자열, 리스트 등등) 이 들어 있으면 True, 비어 있으면 False
print(bool(2))
#--==>> 2
# None은 항상 False

# 문자열에서 + 는 연결 연산자, * 은 반복 연산자
