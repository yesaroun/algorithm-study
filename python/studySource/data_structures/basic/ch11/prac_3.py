f = open("data2.txt")
lines = f.readlines()

hap = 0

for line in lines:
    line = line.rstrip()    # 개행문자제거
    score = int(line)
    hap += score

avg = hap/len(lines)

print("합계:%d" % hap)
print("평균:%5.2f" % avg)

f.close()