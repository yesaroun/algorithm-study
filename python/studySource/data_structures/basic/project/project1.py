# 요구사항 마다 캡쳐하기
# 코드는 3단계에서 완성한 코드 올리기
# 1-3 문장 추가
# 수업일수 부족입니다
# 1-2 추가하기

menu_list = [["콜라", 500], ["사이다", 500], ["환타", 600], ["커피", 600], ["생수", 400]]
money = 0

def menu_price():
    """자판기에서 판매되는 메뉴와 가격을 출력하는 함수"""
    print("** 자판기 판매 메뉴 **")
    print("1 : {} {}".format(menu_list[0][0], menu_list[0][1]))
    print("2 : {} {}".format(menu_list[1][0], menu_list[1][1]))
    print("3 : {} {}".format(menu_list[2][0], menu_list[2][1]))
    print("4 : {} {}".format(menu_list[3][0], menu_list[3][1]))
    print("5 : {} {}".format(menu_list[4][0], menu_list[4][1]))
    print()


def drinking():
    """음료 반환과 잔액 반환 부분을 출력하는 함수"""
    # 메뉴 번호
    menu_num = 6
    global money
    money = int(input("돈을 투입하세요 : "))
    print()

    while menu_num != -1:
        menu_num = int(input("메뉴 선택 (종료:0) : ")) - 1

        if menu_num == -1:
            break
        elif money >= menu_list[menu_num][1]:
            print("{} 구입완료".format(menu_list[menu_num][0]))
            money = money - menu_list[menu_num][1]
            print("잔액: {}".format(money))
            print()
        else:
            print("잔액부족")
            print("잔액: {}".format(money))
            print()

    print("자판기 종료, 잔액 {}반환".format(money))


def change():
    """최종 잔액을 동전으로 교환해주는 함수"""
    global money
    coin500 = 0
    coin100 = 0

    coin500 = money // 500
    coin100 = (money - coin500 * 500) // 100
    remain = money - (500 * coin500) - (100 * coin100)

    print("coin500 : {}개 반환".format(coin500))
    print("coin100 : {}개 반환".format(coin100))
    print("나머지 : {} 반환".format(remain))


if __name__ == "__main__":
    menu_price()
    drinking()
    change()