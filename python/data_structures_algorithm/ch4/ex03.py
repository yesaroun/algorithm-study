class Element:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Element: {self.num}"

    def __repr__(self):
        return self.__str__() + " "

    def __add__(self, other):
        if not isinstance(other, Element):
            raise Exception("should not be different type.")

        add_ = self.num + other.num
        return Element(add_)

    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception("should not be defferent type.")

        sub_ = self.num - other.num
        return Element(sub_)

res = Element(20) - Element(10)
print(res)