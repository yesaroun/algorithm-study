import random
import math 

# 과제 1
"""
num1 = ord('a')
num2 = ord('z')
num_list = []
# print(num2)

for i in range(num1, num2+1):
    num_list.append(i)
# print(num_list)

# print(type(num_list[0]))
result = int

for i in range(10):
    result = random.choice(num_list)
    num_list.remove(result)
    # print(num_list)
    print(chr(result))
"""

# 과제 2
"""
word_list = ["python", "C++", "C", "C#", "java", "javascript", "go"]
result_list = []

for i in range(3):
    result = random.choice(word_list)
    word_list.remove(result)
    result_list.append(result)
    
print(result_list)
"""

# 과제 3
class Circle:
    """원 클래스"""
    pi = math.pi
    def __init__(self, radius: int, name: str) -> None:
        self.radius = radius
        self.name = name
        
    def area(self) -> float:
        """원의 넓이를 구하는 메소드"""
        return self.radius**2 * Circle.pi

    def compare(self, other_circle) -> str:
        """두 원의 크기를 비교하는 메소드"""
        if self.area() > other_circle.area():
            return "{}이(가) {} 보다 {:.3f} 큽니다.".format(self.name, other_circle.name, self.area() - other_circle.area())
        elif self.area() == other_circle.area():
            return "두 원의 크기가 같습니다."
        else:
            return "{}이(가) {} 보다 {:.3f} 큽니다.".format(other_circle.name, self.name, other_circle.area() - self.area())

    def __str__(self) -> str:
        return "{} : 반지름의 길이가 {}이고 넓이가 {:.3f}인 원".format(self.name, self.radius, self.area())
    

circle_1 = Circle(3, 'circle_1')
circle_2 = Circle(10, 'circle_2')
print(circle_1)
print(circle_2)
print(circle_1.compare(circle_2))














