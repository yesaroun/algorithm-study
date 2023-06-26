# [?] n명의 점수 중에서 80점 이상의 점수의 합계

# 합계 알고리즘(Sum Algorithm): 주어진 범위에 주어진 조건에 해당하는 자료들의 합계

# [1] Input(입력): n명의 점수
scores = [100, 75, 50, 37, 90, 95]
sum = 0
N = len(scores)

# [2] Process
for score in scores:
    if score >= 80:
        sum = sum + score

# [3] Output
print(f"{N}명의 점수 중 80점 이상의 총점: {sum}")