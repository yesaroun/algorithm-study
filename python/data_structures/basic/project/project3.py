def add_lst(data):
    global name, tel, email
    name = input("이름:")
    tel = input("연락처:")
    email = input("email:")
    data.append((name, tel, email))
    print(data)

def find_lst(find_name, data):
    for i in data:
        if find_name == name:
            print(find_name, "찾았습니다.")
            break
        else:
            print("해당 정보가 없습니다.")
            break

print("메뉴를 선택하세요")
print("1:추가")
print("3:찾기")
print("0:종료")
data=list()

while True:
    menu = int(input("메뉴선택:"))
    if menu == 1:
        add_lst(data)

    elif menu == 3:
        find_name = input("이름으로 찾기:")
        find_lst(find_name, data)

    elif menu == 0:
        break
    else:
        print("입력오류")