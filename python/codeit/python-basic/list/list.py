# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)

print(numbers)

# numbers에 홀수 제거
start = 0
while start < len(numbers):
    if numbers[start] % 2 == 1:
        del numbers[start]
    else:
        start += 1

print(numbers)

# 0 자리에 20 삽입
numbers.insert(0, 20)
print(numbers)

# 정렬
numbers.sort()
print(numbers)
