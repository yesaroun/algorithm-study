class Term:
    def __init__(self, coef=0, exp=0):
        self.coef = coef
        self.exp = exp

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.coef, self.exp}"

class Polynomial:
    """Polynomial using array."""

    def __init__(self):
        self.bgn = 0
        self.end = 0
        self.terms = []

    def attach(self, coef=0, exp=0):
        self.terms.append(Term(coef, exp))
        return self

    def evaluate(self, x):
        return sum((i.coef * (x ** i.exp) for i in self.terms))

    # -> 이거 없애도 된다.
    '''
    같아지는 케이스는 None을 리턴하고 아닌 경우는 적법한 놈을 찾은 것이다. 
    '''
    def find_term(self, exp) -> Optional[Term]:
        # 제공된 exp 에 상응하는 Term 을 반환한다.
        i = 0
        while i < len(self.terms) and self.terms[i].exp != exp:
            i += 1

        return self.terms[i] if i < len(self.terms) else None


def __str__(self):
        ret = ""
        terms = sorted(self.terms, key=lambda x: x.exp, reverse=True)
        for i in terms:
            ret += f"({i.coef})x^{i.exp} + "
        return f"{ret}\b\b\b"


if __name__ == "__main__":
    poly1 = Polynomial()
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)

    poly2 = Polynomial()
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)

    print()
    poly = poly1 + poly2
    print("poly =\n", poly)