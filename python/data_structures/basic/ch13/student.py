class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def self_introduce(self):
        print("안녕하세요.")
        print("{} {}입니다.".format(self.id, self.name))
        print("만나서 반갑습니다.")

student = Student("kim", 2015)
student.self_introduce()