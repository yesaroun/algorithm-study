# 전역변수(global variable): 함수의 외부에 정의된 변수를 전역변수라고 칭한다.
# 파이썬에서는 전역변수를 다루는 형태가 타 언어들에 비해서 접근방식이라는 측면에서는
# 융통성이 좀 떨어진다.
# 파이썬에서의 위와 같은 부분은 오히려 좋은 프로그래밍 습관을 장려하기 위한 방법론적이다.

def test():
    # test()함수 내에 text라는 지역변수가 없을때는 전역변수를 가져와서 사용함
    print(text)

# test()
#--==>> NameError: name 'text' is not defined.
# test()를 호출한 시점에는 전역변수 text가 정의되어 있지 않기 때문에 에러가 발생
text = "python study"       # 젼역변수인 text변수에 문자열 할당
test()
#--==>> python study

def test():
    print(text)

text = "python study"
test()

def test():
    # 지역변수 text변수에 문자열 할당, 전역변수 text도 할당이 되어 있지만
    # 함수 내에서는 지역변수가 무조건 출력된다. 그 이유는 바로 함 수 내에서는
    # 지역변수가 디폴트이기 때문이다.(중요!)
    text = "파이썬 공부"
    print(text)           # 지역변수 text 값을 출력

test()
#--==>> 파이썬 공부
print(text)
#--==>> python study
# 지역변수 text는 함수 호출후 소멸되었기에 전역변수인 text의 문자열 출력