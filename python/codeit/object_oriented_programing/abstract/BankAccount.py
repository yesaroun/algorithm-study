"""
이것은 docstring입니다.

이렇게 여러 줄을 써도 하나의 docstring입니다.

설명하고자 하는 클래스, 변수, 메소드 아래에 docstring을 작성한다.
"""
class BankAccount:
    """은행 계좌 클래스"""
    interest = 0.02

    def __init__(self, owner_name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balance += amount

    def withdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance *= 1 + BankAccount.interest

# 클래스를 어떻게 사용할 수 있을지 직관적으로 알 수 있다!
