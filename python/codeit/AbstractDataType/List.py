# 파이썬 리스트 생성
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, "연애인 A씨")
trending.insert(1, "잠실 콘서트")
trending.insert(2, "한국 휴일 수")
trending.insert(3, "추석 음식")

print(trending) # 리스트 출력
#--==>> ['연애인 A씨', '잠실 콘서트', '한국 휴일 수', '추석 음식']

# 리스트 접근 연산
# 괄호를 이용한 인덱스 접근
print(trending[0])
print(trending[1])

trending[2] = 4

print(trending)
#--==>>
"""
연애인 A씨
잠실 콘서트
['연애인 A씨', '잠실 콘서트', 4, '추석 음식']
"""

# 탐색 연산
# in을 이용한 탐색
print("연애인 A씨" in trending)     # True
print("연애인 B씨" in trending)     # False

# 삭제 연산
# del을 이용한 삭제
del trending[0]

print(trending)
#--==>> ['잠실 콘서트', 4, '추석 음식']