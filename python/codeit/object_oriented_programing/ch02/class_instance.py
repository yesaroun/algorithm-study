class User:
    def __init__(self, name, email, pw):
        # 유저 인스턴스의 모든 변수를 지정해주는 메소드
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다.".format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

user1 = User("강연훈", "yong@naver.com", "123456")
user2 = User("이윤수", "lee@daum.net", "456789")

print(user1)
print(user2)
#--==>> __str__ 메소드 작성 전
'''
<__main__.User object at 0x102b3bfa0>
<__main__.User object at 0x102b3b670>
# 인스턴스가 어떤 클래스인지 나오고 그 인스턴스가 저장된 메모리 주소가 나온다.
'''
# __str__(던더 str)은 프린트 함수를 호출할때 자동으로 불린다.
#--==>> __str__ 메소드 작성 후
'''
사용자: 강연훈, 이메일: yong@naver.com, 비밀번호: ******
사용자: 이윤수, 이메일: lee@daum.net, 비밀번호: ******
'''