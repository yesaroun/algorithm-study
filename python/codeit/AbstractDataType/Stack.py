from collections import deque

stack = []

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)
#--==>> deque(['T', 'a', 'e', 'h', 'o'])

# 맨 끝 데이터 접근
print(stack[-1])
#--==>> o

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
#--==>>
# o
# h
# e
# deque(['T', 'a'])