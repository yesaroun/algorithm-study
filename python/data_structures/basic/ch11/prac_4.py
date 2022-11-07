f = open("data3.txt")
for line in f:
    line = line.rstrip()
    word = line.split()
    for w in word:
        print(w)

f.close()