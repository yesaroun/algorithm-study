# 함수 선언 부분
def para_func(*para):
    result = 0
    for num in para:
        result += num

    return result

# 전역 변수 선언 부분
hap = 0

#메인 코드 부분
if __name__ == "__main__":
    hap = para_func(10, 20)
    print("hap : %d" % hap)
    hap = para_func(10, 20, 30)
    print("hap : %d" % hap)