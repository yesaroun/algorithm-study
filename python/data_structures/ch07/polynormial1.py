class Polynomial1:
    """Polynomial using array."""
    def __init__(self, degree):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)

    # ::-1은 역을 출력한거다. ret으로 string을 하나 잡고 연결 붙이기를 한거다
    def __str__(self):
        ret = ""
        for coef, exp in [
                             (self.coef[i], i) for i in range(self.degree + 1) if self.coef[i] != 0
                         ][
                         ::-1
                         ]:
            ret += f"({coef})x^{exp} + "

        return f"{ret}\b\b"

    # 방을 21개 만들어놧는데 우리는 값을 채우는거임
    # 리턴할 때 내 몸을 다시 준다.그래서 .attach를 반복해서 쓸 수 있다.
    def attach(self, coef=0, exp=0):
        self.coef[exp] = coef
        return self

    # while문 돌면된다.
    # 뒤에서부터 압쪽으로 할거니까 i를 뽑았다.
    # while문 안에 0이 아닌 놈을 뽑으면 되니까 0 찾으면 된다.
    # 그리고 if문은 못찾았을 때 에러 찾는거임
    # 지수가 가장 큰 값을 찾는 함수
    def get_lead_exp(self):
        i = len(self.coef) - 1
        while i >= 0 and self.coef[i] == 0:
            i -= 1

        if i < 0:
            raise Exception("Failed to get_lead_exp.")
        return i

    # 리스트 안쓰고 이렇게 해도 된다. 리스트가 아니라 이거면 메모리를 덜 쓴다.
    # 계산 함수
    def evaluate(self, x):
        return sum(
            (coef * (x ** exp) for exp, coef in enumerate(self.coef) if coef != 0)
        )

    def get_coef(self, exp):
        return self.coef[exp]

    def is_zero(self):
        return not any(self.coef)
        # any : 값이 뭐라도 있는지 판단하는 함수

    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0

    def remove(self, exp):
        self.coef[exp] = 0


if __name__ == "__main__":

    poly = Polynomial1(20)
    poly.attach(3, 20).attach(2, 5).attach(4, 0)
    print(poly)

    x = 3
    res = poly.evaluate(x)
    print(f"{poly} = {res}, where x = {x}")

    print(poly.get_lead_exp())