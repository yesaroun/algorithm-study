# 문제 : data_list = [(90, 80), (85, 75), (90, 100)] 튜플을 원소로 하는
# 리스트를 활용하여 학생의 총점과 평균(소숫 첫째자리)을 출력하는 프로그램을 작성하시요
# enumerate()함수를 이용한다.
# 출력결과
# 1번 학생의 총점은 170점이고, 평균은 85.0입니다.
# 2번 학생의 총점은 160점이고, 평균은 80.0입니다.
# 3번 학생의 총점은 190점이고, 평균은 95.0입니다.

data_list = [(90, 80), (85, 75), (90, 100)]
# enumerate() 함수의 역할 : 반복문 사용 시 몇 번째 반복을 확인할 때 사용을 한다.
for i, scores in enumerate(data_list):
    # print(i, score)
    hap = 0
    # 학생 1명씩 점수를 누적시킴
    for score in scores:
        hap += score
    print("%d번 학생의 총점은 %d이고, 평균은 %0.1f입니다." % (i+1, hap, hap / 2.0))



