attendance_book = []
attendace = 0
absent = 0

def save(day, att_book):
    """출석부 저장 기능 메서드"""
    if day > 0:
        for i in range(class_count):
            print("{}주차 강의에 출석하셨나요?".format(i + 1))
            day_attendance_book = int(input("출석은 1, 결석은 0 >>>"))
            if day_attendance_book == 0 or day_attendance_book == 1:
                att_book.append(day_attendance_book)
            else:
                raise Exception("잘못된 출석 입력")
    else:
        raise Exception("잘못된 수업 주차 입력")
    # print(att_book)


def count():
    """출석 횟수과 결석 횟수 계산"""
    global attendance_book, attendace, absent
    for i in attendance_book:
        if i == 1:
            attendace += 1
        elif i == 0:
            absent += 1

    print("결석 횟수 : {}".format(absent))
    print("출석 횟수 : {}".format(attendace))

    

def radio_print():
    """출석률과 결석률 계산"""
    global class_count, attendace, absent
    print("결석률은 {}%입니다.".format(round((absent / class_count) * 100)))
    print("출석률은 {}%입니다.".format(round((attendace / class_count) * 100)))
    if round((absent / class_count) * 100) >= 30:
        print("수업 일수 부족입니다.")


class_count = int(input("한 학기 수업주차 입력 : "))

save(class_count, attendance_book)
count()
radio_print()
