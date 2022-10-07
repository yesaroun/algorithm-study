from collections.abc import Iterable

class OddGen:
    def __init__(self, bgn, end):
        self.bgn = bgn
        self.end = end
        self.odd = self.bgn

    def __next__(self):
        if self.odd >= self.end:
            raise StopIteration

        odd = self.odd
        self.odd += 1
        if odd % 2:
            return odd

        return next(self)

    def __iter__(self):
        self.odd = self.bgn
        return self

odd_gen = OddGen(10, 30)

for i in odd_gen:
    print("Odd number: ", i)