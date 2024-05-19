class Student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id
    def __str__(self):
        return "{}학번 {}".format(self.__id, self.name)

student = Student("운상건", 2019)
student.id = 2022
print(student)
