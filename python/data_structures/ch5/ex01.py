
class Person:
    SIZE = 10

    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0

    def __str__(self):
        return f"{self.name}, {self.age}, {self.salary}"

p1 = Person()
p2 = Person()

p1.name = "James"
p1.age = 20
p1.salary = 100.0
p2.name = "Edward"
p2.age = 21
p2.salary = 200.0

print(p1)
print(p2)

# append 함수는 비싼 함수이다. 처음에 비어 있는 메모리를 할당하기 때문 왜냐하면 얼마나 들어올지 모르니까
# 그래서 append 함수를 사용하다보면 처음에 빈 방을 만들었던게 다 차면 또 빈방들을 만듬
# 이런거를 다이나믹 어레이라고 한다.

arr = []
arr.append(p1)
arr.append(p2)

print(arr[0])