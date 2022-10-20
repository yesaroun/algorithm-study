class Array:

    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.items = [None] * capacity

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, item):
        self.items[index] = item


if __name__ == "__main__":
    # Array 객체 instance 를 하나 생성한다. # 기본 크기는 10 개이다.
    arr = Array(5)
    for i in range(len(arr)):
        arr[i] = i

    print(arr)
    index = 3
    print(f"arr[{index}] = {arr[index]}")

    for i in arr:
        print(id(i), i)

    print(sum(arr))
"""
[0, 1, 2, 3, 4] 
arr[3] = 3 
9801216 0 
9801248 1 
9801280 2 
9801312 3 
9801344 4
10
"""