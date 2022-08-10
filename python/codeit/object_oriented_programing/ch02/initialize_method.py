class User:
    def __init__(self, name, email, password):      # 이렇게 메소드 이름 앞에 언더바가 2개 있는 메소드를
    # magic method(special method)라고 한다
    # 우리 말로는 특수 메소드라고 하고 이는 특정 상황에서 자동으로 호출되는 메소드를 말한다.
    # __init__ 메소드는 인스턴스가 생성될 때 자동으로 호출된다.
        self.name = name
        self.email = email
        self.password = password


user1 = User("Young", "young@codeit.kr", "123456")
# 이 줄이 실행되면 User 인스턴스가 생성된다
# 그리고 __init__ 메소드가 자동으로 호출되고 파라미터로 들어간 값들이 순서대로 들어간다.

print(user1.name, user1.email, user1.password)