grades = {}

# key - value 데이터 삽입
grades["kim"] = 80
grades["park"] = 60
grades["choi"] = 90
grades["lee"] = 70
grades["ji"] = 96

print(grades)
#--==>> {'kim': 80, 'park': 60, 'choi': 90, 'lee': 70, 'ji': 96}

# 한 key에 여러 value 저장 시도
grades["park"] = 100

print(grades)
#--==>> {'kim': 80, 'park': 100, 'choi': 90, 'lee': 70, 'ji': 96}

# key를 이용해서 value를 탐색
print(grades["kim"])
print(grades["ji"])
"""
80
96
"""

# key를 이용한 삭제
grades.pop("choi")
grades.pop("lee")

print(grades)
#--==>> {'kim': 80, 'park': 100, 'ji': 96}