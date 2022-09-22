class Polynomial:
    """Polynomial using array."""
    def __init__(self, degree):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)

    def get_lead_exp(self):
        i = len(self.coef) - 1
        while i >= 0 and self.coef[i] == 0:
            i -= 1

        if i < 0:
            raise Exception("Failed to get_lead_exp.")
        return i

    def evaluate(self, x):
        return sum(
            (coef * (x**exp) for exp, coef in enumerate(self.coef) if coef != 0)
        )

    def get_coef(self, exp):
        return self.coef[exp]

    def is_zero(self):
        return not any(self.coef)

    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0

    def attach(self, coef=0, exp=0):
        self.coef[exp] = coef
        return self

    def remove(self, exp):
        self.coef[exp] = 0

    def __str__(self):
        ret = ""
        for coef, exp in [
            (self.coef[i], i) for i in range(self.degree + 1) if self.coef[i] != 0
        ] [
            ::-1
        ]:
            ret += f"({coef})x^{exp} + "

        return f"{ret}\b\b"

    def __add__(self, other: Polynomial):
        poly = Polynomial(max(self.degree, other.degree))

        while not self.is_zero() or not other.is_zero():
            exp_01 = self.get_lead_exp()
            exp_02 = other.get_lead_exp()

            if exp_01 > exp_02:
                # remove 를 적용하여야, lead_exp 의 사용이 의미가 있다.
                #remove에 의해 특정exp의coef가0이 되므로
                # 이후 read_exp 시 다시 읽히는 기회가 사라진다.
                pass
            elif exp_01 < exp_02:
                pass
            else:
                pass

        return poly

if __name__ == "__main__":

    poly1 = Polynomial(2)
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)

    poly2 = Polynomial(1)
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)

    poly = poly1 * poly2
    print()
    print("poly1 * poly2 =\n", poly)