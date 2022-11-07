# 함수 선언 부분
def func1():
    global a
    a = 10
    print("func1()에서 a값 %d" % a)

def func2():
    print("func2()에서 a값 %d" % a)

a = 20

def func3():
    print("func3()에서 a값 %d" % a)

print("a : ", a)

func1()
func2()
func3()
"""
a :  20
func1()에서 a값 10
func2()에서 a값 10
func3()에서 a값 10
"""