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

class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap

    def __setitem__(self, id, elem):
        self.elems[id] = elem

    def __getitem__(self, id):
        return self.elems[id]



elems = Elements()
elems[0] = Element(10)
elems[1] = Element(20)

print(elems[0])
print(elems[1])