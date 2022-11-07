f = open("name.txt")
while True:
    data = f.readline()
    if not data:
        break
    print(data, end="")

f.close()