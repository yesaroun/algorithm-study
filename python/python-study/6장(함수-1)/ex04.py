# 섭씨 온도를 화씨 온도로 변환하여 반환하는 함수 FtoC()를 작성하시오.

# 함수 선언 및 구현
def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32.0))/9.0
    return temp_c


temp_f = float(input("화씨온도를 입력해주세요 : "))
# 함수 호출
print("화씨 온도인", temp_f, "를 섭씨 온도로 변환한 값 : ", round(FtoC(temp_f), 2))
#--==>>
'''
화씨온도를 입력해주세요 : 20
화씨 온도인 20.0 를 섭씨 온도로 변환한 값 :  -6.67
'''