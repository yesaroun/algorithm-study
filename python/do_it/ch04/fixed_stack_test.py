# 고정 길이 스택 클래스(FixedStack)를 사용하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    '''메뉴 선택'''
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='     ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)          # 최대 64개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    menu = select_menu()    # 메뉴 선택

    if menu == Menu.푸시:     # 푸시
        x = int(input("데이터를 입력하세요.:"))