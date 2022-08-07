class User:
    def say_hello(self):
        # 인사 메시지 출력 메소드
        print("안녕하세요! 저는 {}입니다.".format(self.name))

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디거나 잘못된 비밀번호입니다.")

user1 = User()

user1.name = "김대위"
user1.email = "captain@aa.com"
user1.password = "12345"

user1.login(user1, "captain@aa.com", "12345")
user1.login("captain@aa.com", "12345")

# 인스턴스 메소드의 주인공은 첫번째 파라미터로 들어오는 인스턴스이다.
# 이렇게 첫 번째 파라미터를 self로 써주면 주인공이 항상 self라는 걸 알기 때문에 훨씬 읽기 편한 코드가 된다.
# 다른 단어를 써도 아무런 문제는 없다