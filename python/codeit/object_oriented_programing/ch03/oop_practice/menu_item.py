class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return ("{} 가격: {}".format(self.name, self.price))

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)
#--==>>
'''
햄버거 가격: 4000
콜라 가격: 1500
후렌치 후라이 가격: 1500
'''