# 지역변수(local variable)와 전역변수(global variable)에 대한 실습
# 지역 변수 : 파이썬에선느 함수 안에 정의된 변수를 지역변수라고 하며, 지역변수의 범위(scope)은
# 함수 내에서만 사용이 되고 함수가 호출이 되고 종료가 되면 지역변순느 소멸된다.

def test():
    text = "파이썬 공부"     # 지역 변수 text에 문자열 할당
    print(text)           # 출력함수를 이용하여 text를 출력함

# test()를 호출한 후, "파이썬 공부"라는 문자열을 출력하면서 리턴값은 없다.
test()
#--==>> 파이썬 공부

def test():
    text = "파이썬 공부"     # 지역 변수 범위는 test() 내에서만 사용
    print(text)

test()
# 아래 출력함수에서 NameError: name 'text' is not defined 에러코드가 발생한다.
# 이유는 바로 text 변수가 정의되지 않았다.
# 아울러, test()에 있는 text라는 변수는 지역변수이므로 함수 호출 후 소멸된다.
# print(text)

