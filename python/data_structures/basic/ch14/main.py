# 과제1
# class Rectangle:
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#
#     def calcArea(self):
#         return self.h * self.w
#
#     def __str__(self):
#         return "사격형의 폭: {}, 높이: {}, 면적: {}".format(self.w, self.h, self.calcArea())
#
# rec1 = Rectangle(0, 0, 100, 100)
# print(rec1)
# rec2 = Rectangle(10, 10, 200, 200)
# print(rec2)


# 과제2
# class Dog:
#     def __init__(self, name, tricks):
#         Dog.kind = "black dog"
#         self.name = name
#         self.tricks = tricks
#
# dog1 = Dog("lee", ["뒹굴기", "달리기"])
# print(dog1.tricks)


# 과제3
class BankAccount(object):
    interest_rate = 0.3  # 클래스 변수

    def __init__(self, name, number, balance):
        # 인스턴스 변수들
        self.name = name
        self.number = number
        self.balance = balance
        return

    def withdraw(self, money):
        self.balance += money

    def deposit(self, money):
        if self.balance < money:
            print("잔고보다 더 큰 금액을 인출할 수 없습니다.")
        else:
            self.balance -= money


class StudentAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)

    def withdraw(self, money):
        super().withdraw(money)

    def deposit(self, money):
        if self.balance + 100000 < money:
            print("해당 금액을 인출할 수 없습니다.")
        else:
            self.balance -= money


student1 = StudentAccount("kim", 1, 100)
student1.deposit(10000)
print("student1의 잔고 : ", student1.balance)

bank1 = BankAccount("lee", 1, 100)
bank1.deposit(10000)
