# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)

# 13초를 늘린다
for i in range(13):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)

# 23시 59분 57초로 세팅
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()

# 시계의 현재 시간 출력
print(clock)