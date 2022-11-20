
class ThisSemesterCalculator:
    """이번 학기 평점 평균 계산"""
    def __init__(self):
        # 수강 정보 리스트
        self.score = []
        # 총 학점 수
        self.total_sub_count = 0
        # 총 점수의 총합
        self.total_sub_score = 0
        # 평균 점수
        self.avg_score = 0
        # 장학 여부
        self.scholarship = False

    def import_score_list(self):
        sub_name = input("과목명을 입력하세요: ")
        sub_count = eval(input("학점수를 입력하세요: "))
        # 학점 범위 확인
        if not (1 <= sub_count <= 6):
            print("올바른 학점을 입력하세요\n")
            return
        sub_score = input("취득학점을 입력하세요(A+ ~ F): ")
        # 입력받은 학점 대문자로 변환
        sub_score = sub_score.upper()
        if not (sub_score == "A+" or sub_score == "A" or sub_score == "B+" or sub_score == "B"
                or sub_score == "C+" or sub_score == "C" or sub_score == "D+" or sub_score == "D"
                or sub_score == "F"):
            print("올바른 점수를 입력하세요\n")
            return

        self.score.append([sub_name, sub_count, sub_score])
        return

    def score_avg_calc(self):
        for i in self.score:
            # 총 수강 학점
            self.total_sub_count += i[1]

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

            self.total_sub_score += i[1] * sub_calc_score

        avg_score = self.total_sub_score / self.total_sub_count

        if avg_score >= 4.0:
            self.scholarship = True

        # print(total_sub_score, total_sub_count)
        print("평균 학점: ", avg_score)

        if self.scholarship:
            print("학기별 장학 대상자입니다.")


class AllSemesterCalculator:
    """전체 학기 평점 평균 계산"""
    def __init__(self):
        # 졸업 대상자 확인
        self.graduation_req = True
        # 졸업 장학 대상자 확인
        self.scholarship = False
        self.message = "졸업 미충족 사유\n"

    def graduation_requirements_print(self):
        print("--졸업요건--")
        print("1.총 등록학기 8학기 이상\n2.총 학점수 120학점 이상\n총 평균평점 2.5이상\n")

    def graduation_requirements_check(self):
        total_semester = eval(input("총 등록학기를 입력하세요: "))
        total_sub = eval(input("총 학점수를 입력하세요: "))
        total_score = eval(input("총 평균평점을 입력하세요: "))

        if total_semester < 8:
            self.graduation_req = False
            self.message += "학기 부족\n"

        if total_sub < 120:
            self.graduation_req = False
            self.message += "졸업학점 부족\n"

        if total_score < 2.5:
            self.graduation_req = False
            self.message += "졸업 평균평점 부족\n"
        elif total_score >= 4.0:
            self.scholarship = True

    def graduation_status_check(self):
        if self.graduation_req and self.scholarship:
            print("졸업 장학 대상자입니다.")
        elif self.graduation_req:
            print("졸업 대상자입니다.")
        else:
            print(self.message)



if __name__ == "__main__":
    print("-- 초간단 평점 평균 계산 시스템 --")

    this_semester_calc = ThisSemesterCalculator()
    all_semester_calc = AllSemesterCalculator()
    check = True

    while check:
        num1 = eval(input("1.이번 학기 학점 계산 2.전체 학기 학점 계산 0.종료: "))
        if num1 == 0:
            check = False
        elif num1 == 1:
            this_semester_calc.import_score_list()
            check1 = True

            while check1:
                num2 = eval(input("1.계속 수강정보 추가하기 2.평균 계산하기 0.종료: "))
                if num2 == 1:
                    this_semester_calc.import_score_list()
                elif num2 == 2:
                    this_semester_calc.score_avg_calc()
                elif num2 == 0:
                    check1 = False
                else:
                    print("올바른 숫자를 입력하세요.\n")

        elif num1 == 2:
            check2 = True

            while check2:
                num3 = eval(input("1.졸업요건 출력 2.내 학적 정보 저장하기 3.내 졸업 여부 확인하기 0.종료: "))
                if num3 == 0:
                    check2 = False
                elif num3 == 1:
                    all_semester_calc.graduation_requirements_print()
                elif num3 == 2:
                    all_semester_calc.graduation_requirements_check()
                elif num3 == 3:
                    all_semester_calc.graduation_status_check()
                else:
                    print("올바른 숫자를 입력하세요.\n")

        else:
            print("올바른 숫자를 입력하세요.\n")

