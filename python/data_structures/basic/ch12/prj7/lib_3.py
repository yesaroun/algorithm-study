library = []

f = open("전국도서관표준데이터.csv", "r", encoding="euc-kr")
lines = f.readlines()

# 도서관 정보 리스트에 저장(도서관명, 시도명, 시군구명)
for line in lines:

    temp = line.split(",")
    library_sep = [temp[0], temp[17], temp[19]]
    # library_sep = []
    # library_sep.append(temp[0])
    # library_sep.append(temp[17])
    # library_sep.append(temp[19])

    library.append(library_sep)

while True:
    # 검색된 도서관을 저장하는 리스트
    searched_library = []

    search = input("검색어 입력(종료:0): ")

    if search == "0":
        print("프로그램이 종료됩니다.")
        break

    print("\n[도서관 정보 검색 결과]")
    for i in library:
        searched_word = i[1].split(" ")
        for j in searched_word:
            if search == j:
                searched_library.append(i)
                # print(i)

    searched_library.sort(key=lambda a:a[0])
    for i in searched_library:
        print(i)
    print()

f.close()