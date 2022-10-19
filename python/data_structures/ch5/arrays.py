class Array:
    SIZE = 11

    def __init__(self, data):
        self.data = [i for i in range(data)]

    def __str__(self):
        return f"{self.data}"

    # def __len__(self):
    #     while i is not None:


if __name__ == "__main__":
    # Array 객체 instance 를 하나 생성한다.
    # 기본 크기는 10 개이다.
    arr = Array(5)

    # for i in range(len(arr)):
    #     arr[i] = i
    for i in range(5):
        arr[i] = i

    print(arr)
    index = 3
    print(f"arr[{index}] = {arr[index]}")

    for i in arr:
        print(id(i), i)

    print(sum(arr))