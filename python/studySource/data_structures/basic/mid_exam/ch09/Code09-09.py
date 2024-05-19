# 함수 선언 부분
def multi(v1, v2):
    retList = []    # 반활할 리스트
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

# 전역 변수 선언 부분
myList = []
hap, sub = 0, 0

if __name__ == "__main__":
    myList = multi(100, 200)
    hap = myList[0]
    sub = myList[1]
    print("%d, %d" % (hap, sub))