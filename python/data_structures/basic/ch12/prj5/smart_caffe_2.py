menu= [['에스프레소',2000,'커피'],['아메리카노',2500,'커피'],['카푸치노',3000,'커피'],
['카페라떼',3000,'커피'],['모카라떼',3500,'커피'],['바닐라라떼',3500,'커피'],
['소이라떼',3500,'커피'],['피넛라떼',3700,'커피'],['토피넛라떼',3700,'커피'],
['화이트모카',3700,'커피'],['카라멜마끼아또',4000,'커피'],['프라프치노',4000,'커피'],
['핫초코',3500,'음료'],
['레몬에이드',3500,'음료'],['청포도에이드',3500,'음료'],['자몽에이드',3500,'음료'],
['스무디',3500,'음료'],['망고스무디',3500,'음료'],['딸기스무디',3500,'음료'],
['초코쿠키',2000,'디저트'],['화이트쿠키',2000,'디저트'],['피넛쿠키',2000,'디저트'],
['당근케이크',5000,'디저트'],['초코케이크',5000,'디저트'],['치즈케이크',5000,'디저트']]

# 주문된 내역
choiced_result = []
# 총 가격
choiced_price = 0

print("[스마트 카페 메뉴 목록]\n")
# 메뉴 리스트 출력
temp = 0
for i in menu:
    print(i[0], end=" ")
    temp += 1
    if temp % 10 == 0:
        print("")
print("\n")

while True:
    choice = eval(input("1.가격별 메뉴 조회 2.종류별 메뉴 조회 3.주문 0.종료: "))
    result = []
    if choice < 0 or choice > 3:
        print("없는 번호!")
        continue

    elif choice == 1:
        min, max = eval(input("최저가격, 최고가격 입력(예:1000, 2000): "))
        for i in menu:
            if min <= i[1] <= max:
                result.append(i[:2])

    elif choice == 2:
        category = input('종류별 메뉴 입력(예:커피,음료,디저트): ')
        for i in menu:
            if i[2] == category:
                result.append(i[:2])

    elif choice == 3:   # 주문
        menu_count = 0

        while True:
            order = input("주문 메뉴 입력(0:종료): ")
            temp_ordered = []
            if order == "0":
                break

            for i in menu:
                if i[0] == order:
                    temp_ordered = (i[:2])

            # 올바르지 않은 메뉴 입력했을 경우
            if len(temp_ordered) == 0:
                print("올바른 메뉴를 입력하세요.\n")
                continue
            else:
                while True:
                    count = eval(input("수량 입력: "))

                    # 올바르지 않은 수량 입력했을 경우
                    if count <= 0:
                        print("올바른 수량을 입력하세요.\n")
                        continue
                    else:
                        # 같은 주문 내역이 있는지 확인하는 변수
                        same_checker = False

                        temp_ordered.append(count)
                        for i in choiced_result:
                            if i[0] == temp_ordered[0]:
                                same_checker = True
                                i[2] = i[2] + count

                        if same_checker is False:
                            choiced_result.append(temp_ordered)

                        break

    elif choice == 0:
        print("스마트 카페 메뉴조회 시스템 종료!")
        break

    if choice == 3:
        print("\n 주문 내역 확인:", end=" ")
        print()
        print(choiced_result)
        # 합계 가격 구하기
        # 합계 금액 초기화 해줘야 한다.
        choiced_price = 0
        for i in choiced_result:
            # print(i[2])
            choiced_price += (i[1] * i[2])

        print("지불 총금액: {}원".format(choiced_price), end="\n\n")

    # 주문하지 않은 경우
    else:
        print("\n 입력조건의 메뉴 목록>")
        print(result, end="\n\n")

