f = open("name.txt")
data = f.readlines()
for line in data:
    print(line, end="")

f.close()