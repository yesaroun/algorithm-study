f = open("guest.txt", "w")
while True:
    name = input("name : ")
    if not name:break
    print("{} welcome!".format(name))
    f.write(name + "")
f.close()

f = open("guest.txt")
lines = f.readlines()
cnt = len(lines)
print("total count : {}".format(cnt))