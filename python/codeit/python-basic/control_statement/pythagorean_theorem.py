for a in range(1, 398):
    for b in range(1, 398):
        c = 400 - a - b
        if a < b < c and a * a + b * b == c * c:
            print(a * b * c)

