# 추상화의 좋은 예시
class BankAccount:
    interest = 0.02

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + BankAccount.interest

# 어디에 쓰는 클래스이고 어떻게 사용할지 직관적으로 알 수 있다.

example_account = BankAccount("Hong Gil dong", 1000)

example_account.add_interest()
print(example_account.balance)
#--==>> 1020.0

example_account.deposit(500)
print(example_account.balance)
#--==>> 1520.0

example_account.withdraw(2000)
#--==>> Insufficient balance!
example_account.withdraw(1000)

print(example_account.balance)
#--==>> 520.0