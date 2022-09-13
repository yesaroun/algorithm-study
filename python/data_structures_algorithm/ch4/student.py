class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name is : {self.name}, {self.age}"

st = Student("Gildong Hong", 20)
print(st)
# __init__ 메소드만 있을때
#--==>> <__main__.Student object at 0x101103fd0>

# __str__메소드가 있을때
#--==>> name is : Gildong Hong, 20