class Citizen:
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        return self.resident_id == id_field

    def can_drink(self):
        return self.age >= Citizen.drinking_age

    def __str__(self):
        return self.name + "씨는 " + str(self.age) + "살입니다!"

    # getter 메소드 역할을 한다.
    @property
    def age(self):
        print("나이를 리턴합니다.")
        return self._age

    # setter 메소드 역할을 한다.
    @age.setter
    def age(self, value):
        print("나이를 설정합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value


young = Citizen("kim", 15, "12345")
print(young.age)
young.age = 30
print(young.age)