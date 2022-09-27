class Element:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Element: {self.num}"

    # def __repr__(self):
    #     return self.__str__() + " "

    def __repr__(self):
        return str(self)

elems = [Element(100), Element(200)]
print(elems)
#--==>> [Element: 100, Element: 200]