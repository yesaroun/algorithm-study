SIZE = 21

arr = [i for i in range(1, SIZE)]

print("   addr    \tvalue")

for i in arr:
    print(f"{id(i):8}\t{i:2}")



