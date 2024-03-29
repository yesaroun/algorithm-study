# [?] n명의 점수 중에서 80점 이상의 점수의 합계

# 합계 알고리즘(Sum Algorithm): 주어진 범위에 주어진 조건에 해당하는 자료들의 합계

# [1] Input(입력): n명의 점수
scores: list[int] = [100, 75, 50, 37, 90, 95]
sum: int = 0  # 합계가 저장될 그릇
N: int = len(scores)  # 의사코드(슈도코드)

# [2] Process(처리): 합계 알고리즘 영역: 주어진 범위에 주어진 조건(필터링)
for i in range(0, N):  # 주어진 범위
    if scores[i] >= 80:  # 주어진 조건
        sum = sum + scores[i]  # SUM

# [3] Output
print(f"{N}명의 점수 중 80점 이상의 총점: {sum}")
