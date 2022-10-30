class Employee:
    """직원 클래스"""
    company_name = "버거집"      # 가게 이름
    raise_percentage = 1.03   # 시급 인상률

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name    # 이름
        self.wage = wage    # 시급

    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name

class Cashier(Employee):
    raise_percentage = 1.05
    buger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_recived):
        """주문과 돈을 받고 거스름돈을 리턴한다."""
        if Cashier.buger_price > money_recived:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_recived
        else:
            self.number_sold += 1
            change = money_recived - Cashier.buger_price
            return change

    def __str__(self):
        return Cashier.company_name + "계산대 직원: " + self.name

class DeliveryMan(Employee):
    """배달원 클래스"""

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name

# Cashier 클래스와 deliveryMan 클래스를 다중 상속 받는 클래스 생성
class CashierDeliveryMan(DeliveryMan, Cashier):
    def __init__(self, name, wage, on_standby, number_sold=0):
        Employee.__init__(self, name, wage)
        self.on_standby = on_standby
        self.number_sold = number_sold

# 이 상태에서 아래 코드를 실행하면
cashier_and_deleivery_man = CashierDeliveryMan("kim", 7000, True, 10)
print(cashier_and_deleivery_man)
#--==>> 버거집 배달원: kim
# 어떤 __str__ 메서드가 실행되어야 할지 애매한 상황이다.
print(CashierDeliveryMan.mro())
#--==>> [<class '__main__.CashierDeliveryMan'>, <class '__main__.DeliveryMan'>, <class '__main__.Cashier'>, <class '__main__.Employee'>, <class 'object'>]
# 이 순서로 실행되니까 DeliveryMan 클래스가 먼저 실행되었다.
# 만약 class CashierDeliveryMan(Cashier, DeliveryMan):
# 이 순서일 경우는 Cashier 클래스가 먼저 실행된다.
