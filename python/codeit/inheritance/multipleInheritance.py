# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print("{}(으)로 프로그래밍합니다.".format(self.favorite_language))

# 테니스 선수 클래스
class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다.".format(self.tennis_level))


# 엔지니어이면서 테니스 선수이라면 이때 다중상속하면 된다.
class EnginnerTennisPlayer(Engineer, TennisPlayer):
    def __init__(self, favorite_language, tennis_level):
        # 여기서 super를 쓸 경우 어느 부모를 나타내는지 알 수 없는 다중 상속의 단점이 나온다.
        Engineer.__init__(self, favorite_language)
        TennisPlayer.__init__(self, tennis_level)

# 다중 상속을 받는 클래스의 인스턴스 생성
lee = EnginnerTennisPlayer("python", "초급")

# 두 부모 클래스의 메소드들을 잘 물려받았는지 확인
lee.program()
lee.play_tennis()
"""
python(으)로 프로그래밍합니다.
초급 반에서 테니스를 칩니다.
"""