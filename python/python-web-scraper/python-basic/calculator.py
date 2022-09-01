def plus(a=0, b=0):
    print("Result: ", a + b)

def minus(a=0, b=0):
    print("Result: ", a - b)

def multi(a=1, b=1):
    print("Result: ", a * b)

def divide(a=1, b=1):
    print("Result: ", a / b)


playing = True

while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input("Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")

    if operation == "exit":
        playing = False
    elif operation == "+":
        plus(a, b)
    elif operation == "-":
        minus(a, b)
    elif operation == "*":
        multi(a, b)
    elif operation == "/":
        divide(a, b)
    else:
        break