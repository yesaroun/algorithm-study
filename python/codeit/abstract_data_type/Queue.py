# deque는 파이썬 collections 모듈에서 가지고 온다.
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("kim")
queue.append("park")
queue.append("lee")
queue.append("cho");

print(queue)
#--==>> deque(['kim', 'park', 'lee', 'cho'])

# 큐의 가장 앞 데이터에 접근
print(queue[0])
#--==>> kim

# 큐 맨 앞 데이터 삭제
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)
#--==>>
# kim
# park
# lee
# deque(['cho'])
