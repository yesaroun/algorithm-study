# import csv

# with open("전국도서관표준데이터.csv", newline="", encoding='euc-kr') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter = " ", quotechar="|")
#     for row in spamreader:
#         print(", ".join(row))

library = []

f = open("전국도서관표준데이터.csv", "r", encoding="euc-kr")
lines = f.readlines()

# 도서관 정보 리스트에 저장(도서관명, 시도명, 시군구명)
for line in lines:
    # print(line)
    # 대화도서관,경기도,고양시,공공도서관
    # print(line.split(","))
    # 서창한옥작은도서관', '광주광역시', '서구', '작은도서관', '"매주월요일',
    temp = line.split(",")
    library_sep = []
    library_sep.append(temp[0])
    library_sep.append(temp[17])
    library_sep.append(temp[19])
    # for i in range(3):
    #     library_sep.append(temp[i])
    library.append(library_sep)
# print(library)
# [['제남도서관', '제주특별자치도', '서귀포시'], ['서귀포시삼매봉도서관', '제주특별자치도', '서귀포시'], ['서귀포시중앙도서관', '제주특별자치도', '서귀포시']]
# [['서귀포시삼매봉도서관', '제주특별자치도 서귀포시 남성중로153번길 15', '064-733-1524'], ['서귀포시중앙도서관', '제주특별자치도 서귀포시 김정문화로 32', '064-739-1516']]


while True:
    search = input("검색어 입력(종료:0): ")

    if search == "0":
        print("프로그램이 종료됩니다.")
        break

    print("\n[도서관 정보 검색 결과]")
    for i in library:
        searched_word = i[1].split(" ")
        # print(searched_word)
        for j in searched_word:
            if search == j:
                print(i)
    print()

f.close()