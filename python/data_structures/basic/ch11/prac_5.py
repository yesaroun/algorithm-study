vote = {"가평":0, "LA":0, "NY":0}
print(vote)

print("Best MT Spot")
while True:
    area = input("area:")
    if not area:
        break
    vote[area] = vote[area] + 1     # 키 값 증가

print(vote)