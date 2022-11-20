
print("수강 강좌정보 입력")

# 수강 정보 리스트
score = []
# 총 학점 수
total_sub_count = 0
# 총 점수의 총합
total_sub_score = 0
# 평균 점수
avg_score = 0

while True:
    choice = eval(input("1.수강 강좌정보 입력하기 2.평균 확인하기 0.종료: "))

    if choice == 0:
        break
    elif choice == 1:
        sub_name = input("과목명을 입력하세요: ")
        sub_count = eval(input("학점수를 입력하세요: "))
        # 학점 범위 확인
        if not(1 <= sub_count <= 6):
            print("올바른 학점을 입력하세요\n")
            continue
        sub_score = input("취득학점을 입력하세요(A+ ~ F): ")
        # 입력받은 학점 대문자로 변환
        sub_score = sub_score.upper()
        if not(sub_score == "A+" or sub_score == "A" or sub_score == "B+" or sub_score == "B"
            or sub_score == "C+" or sub_score == "C" or sub_score == "D+" or sub_score == "D"
            or sub_score == "F"):
            print("올바른 점수를 입력하세요\n")
            continue

        score.append([sub_name, sub_count, sub_score])

    elif choice == 2:
        # test
        # print(score)

        for i in score:
            # 총 수강 학점
            total_sub_count += i[1]

            # 학점 계산
            sub_calc_score = 0
            if i[2] == "A+":
                sub_calc_score = 4.5
            elif i[2] == "A":
                sub_calc_score = 4.0
            elif i[2] == "B+":
                sub_calc_score = 3.5
            elif i[2] == "B":
                sub_calc_score = 3.0
            elif i[2] == "C+":
                sub_calc_score = 2.5
            elif i[2] == "C":
                sub_calc_score = 2.0
            elif i[2] == "D+":
                sub_calc_score = 1.5
            elif i[2] == "D":
                sub_calc_score = 1.0
            else:
                # f인 경우
                sub_calc_score = 0

            total_sub_score += i[1] * sub_calc_score

        avg_score = total_sub_score / total_sub_count

        # print(total_sub_score, total_sub_count)
        print("평균 학점: ", avg_score)

    else:
        print("올바른 숫자를 입력하세요.\n")