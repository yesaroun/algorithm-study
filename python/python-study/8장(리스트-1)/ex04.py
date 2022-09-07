# 시퀀스 자료형 : 순서를 가지는 요소들로 구성된 자료형을 의미한다.
# 문자열, 바이트 시퀀스, 바이트 배열, 리스트, 튜플, range() 객체가 존재한다.
# 시퀀스 자료형의 특징
# 1. 요소들이 순서를 가지고 있다.
# 2. 인덱스를 이용하여 요소들을 참조할 수 있다.

# 문자열에 대한 참조
words = "Nice To Mett You!"
print(words[0], words[5], words[-1])

li = ["apple", "banana", "peach", "tomato"]
# print(li[5])
# 이 출력 코드는 없는 인덱스를 참조하므로 에러가 발생한다.
# IndexError: list index out of range

# 시퀀스의 길이를 구하는 코드
print("words의 길이 : ", len(words))
print("li의 길이 : ", len(li))

# 시퀀스에서 가능한 연산과 함수
li1 = [1, 2]
print("li1의 주소값 : ", id(li1))
li2 = [3, 4, 5]
print("li2의 주소값 : ", id(li2))
# 시퀀스 자료형은 + 연산이 가능하다.
li3 = li1 + li2
print("li3의 주소값 : ", id(li3))
# * 연산자는 시퀀스 자료형에 해당하는 값을 반복시켜서 요소의 수가 증가가 됨
print(["안녕", "hi"] * 3)

# in 연산자는 시퀀스 자료형에 해당하는 값이 있다면 True 를 반환
print(10 in [10, 2, 3])

# not in 연산자는 시퀀스 자료형에 해당하는 값이 있다면 False를 반환
print(10 not in [10, 2, 3])

# 시퀀스 자료형의 최대값
print(max([10, 2, 3]))

# 시퀀스 자료형의 최솟값
print(min([10, 2, 3]))

# 반복문의 시퀀스 자료형이 올 수가 있다.
for i in "일이삼":
    print(i)