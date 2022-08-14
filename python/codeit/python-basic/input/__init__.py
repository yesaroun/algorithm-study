name = input("이름을 입력하세요 : ")
# 입력값을 name 변수에 저장
print(name)

x = input("숫자를 입력하세요 : ")
print(x + 5)
# 에러 발생
# input 함수가 받는 값은 항상 문자열이다!

x = int(input("숫자를 입력하세요 : "))      # 정수로 변환
print(x + 5)