class User:
    def say_hello(some_user):
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(some_user.name))

        # say_hello는 인스턴스 변수(some_user)를 사용하기에 인스턴스 변수라고 할 수 있다.


user1 = User()
user2 = User()
user3 = User()

user1.name = "김대위"
user1.email = 'captin@codeit.kr'
user1.password = '12345'

user2.name = '강영훈'
user2.email = 'younghoon@codeit.kr'
user2.password = '98777'

user3.name = '최지웅'
user3.email = 'jiwoong@codeit.kr'
user3.password = '78945'

User.say_hello(user1)
user1.say_hello()       # 파라미터를 넘겨주지 않아도 에러가 나지 않음 이건 인스턴스 메소드의 특별한 규칙 때문
# 윗줄은 클래스에서 메소드 호출했고 아랫줄은 인스턴스의 메소드를 호출했다.
# 인스턴스에 메소드를 호출하면 user1인스턴스가 say_hello의 첫번째 파라미터로 자동으로 전달되서 파라미터를 따로 써줄 필요가 없다.
# 그래서 윗줄, 아랫줄은 똑같다.
# user1.say_hello(user1)
# 이렇게 하면 에러 발생
# TypeError: say_hello() takes 1 positional argument but 2 were given
# say_hello()는 파라미터를 한개만 받는데 2개를 받았다는 에러 왜냐하면 자동으로 전달되기 때문


