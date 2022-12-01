# 문제1
"""
import random

rock_si_list = ['가위', '바위', '보']


check = False
result = "" # 마지막 출력문
finshed_game = True     # 게임 끝내는 변수
com_win = 0     # 컴퓨터 이기는 승 수
user_win = 0    # 사람 이기는 승 수 


def check_winner(user_win, com_win):
    if user_win >= 3:
        print("당신 3승!")
        return False
    elif com_win >= 3:
        print("컴퓨터 3승!")
        return False
    else:
        return True



while finshed_game:
    com_choice = random.choice(rock_si_list)
    
    user_choice = input("가위, 바위, 보 중 하나를 입력하시오: ")
    # 가위, 바위, 보 확인
    for i in rock_si_list:
        if i == user_choice:
            check = True
    if not check:
        result = "입력 오류"
    else:
        print("컴퓨터: ", com_choice)
        if com_choice == "가위":
            if user_choice == "가위":
                result = "비겼습니다"
            elif user_choice == "바위":
                result = "당신 승"
                user_win = user_min + 1
            else:
                result = "컴퓨터 승"
                com_win = com_win + 1
        elif com_choice == "바위":
            if user_choice == "가위":
                result = "컴퓨터 승"
                com_win = com_win + 1
            elif user_choice == "바위":
                result = "비겼습니다"
            else:
                result = "당신 승"
                user_win = user_win + 1
        else:       # 보 
            if user_choice == "가위":
                result = "당신 승"
                user_win = user_win + 1
            elif user_choice == "바위":
                result = "컴퓨터 승"
                com_win = com_win + 1
            else:
                result = "비겼습니다"
    print(result)
    
    finshed_game = check_winner(user_win, com_win)
    
"""


# 문제2

num1 = input("1.암호화 2.암호해석 중 선택: ")

if num1 == "1":
    i_name = input("입력 파일명을 입력하세요: ")
    i_name = i_name + ".txt"
    o_name = input("출력 파일명을 입력하세요: ")
    o_name = o_name + ".txt"

    try:
        result = ""
        # print(1)
        i = open(i_name, "r")
        o = open(o_name, "w")
        # print(2)
        for line in i:
            line = line.rstrip()
            word = line.split()
            for w in word:
                for spel in w:
                    # print(spel)
                    num = ord(spel)
                    num = num + 1
                    text = chr(num)
                    # print(text)
                    result = result + text
                    # result = result + (",")
                result = result + ("n")

        # print(result)
        o.write(result)
        i.close()
        o.close()
        print("{} --> {} 변환 완료".format(i_name, o_name))
    except:
        print("파일이 없습니다.")
elif num1 == "2":
    i_name = input("입력 파일명을 입력하세요: ")
    i_name = i_name + ".txt"
    o_name = input("출력 파일명을 입력하세요: ")
    o_name = o_name + ".txt"

    try:
        result = ""
        i = open(i_name, "r")
        o = open(o_name, "w")
        for line in i:
            line = line.rstrip()
            line = line.split("/n")
            for word in line:
                word = word.split("n")
                for w in word:
                    for spel in w:
                        num = ord(spel)
                        num = num - 1
                        text = chr(num)
                        result = result + text
                    result = result + " "
                result = result + "\n"
            # print(result)

        o.write(result)
        i.close()
        o.close()
        print("{} --> {} 변환 완료".format(i_name, o_name))
    except:
        print("파일이 없습니다.")















