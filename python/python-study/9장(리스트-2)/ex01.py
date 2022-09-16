# list 복사하기
# 얕은 복사(shallow copy) : 주소값을 공유하는 개념, 원본 리스트에 영향을 끼치는 복사 방법,
#                           엄밀히 이야기하면 진정한 복사가 아니다.

scores = [10, 20, 30, 40, 50]
refer = scores      # scores의 주소값을 refer 변수에게 복사
print("scores의 주소값 : ", id(scores))
print("refer의 주소값 : ", id(refer))
refer[0] = 100
refer.append(-70)
refer.insert(1, -100)
print("scores의 주소값 : ", id(scores))
print("refer의 주소값 : ", id(refer))

print("scores의 요소값 : ", scores)
print("refer의 요소값 : ", refer)
'''
scores의 주소값 :  4350420928
refer의 주소값 :  4350420928
scores의 주소값 :  4350420928
refer의 주소값 :  4350420928
scores의 요소값 :  [100, -100, 20, 30, 40, 50, -70]
refer의 요소값 :  [100, -100, 20, 30, 40, 50, -70]
'''