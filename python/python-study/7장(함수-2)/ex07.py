# 지역변수와 전역변수의 실습

# def test():
#     # 함수 안에서 하나의 변수가 전역변수가 되었다가 다시 지역변수가 될 수가 없는 것이다. 그래서 아랫줄 에러난다.
#     print(text)
#     text = "python study"
#     print(text)
#
# text = "java study"
# test()
# #--==>> UnboundLocalError: local variable 'text' referenced before assignment
# print(text)

# 전역변수를 함수 안에서 값을 변경하고자 한다면... global 키워드를 명시적으로
# 함수 안에 적어줘야 한다.
def test():
    global text     # test()함수 안에서 전역변수인 text를 사용하겠다라는 것을 인터프리터한테 알린다.
    print(text)
    text = "python study"   # 젼역 변수의 값을 변경하고 있다.
    print(text)

text = "java study"
test()
print(text)
#--==>>
'''
java study
python study
python study
'''