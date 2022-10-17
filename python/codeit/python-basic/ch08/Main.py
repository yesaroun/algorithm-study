# 문제1
# def greet(lang):
#     if lang == 1:
#         print('Hola')
#     elif lang == 2:
#         print("Bonjour")
#     elif lang == 3:
#         print("안녕")
#     else:
#         print("지원하지 않습니다.")
#
# h = int(input("언어를 선택하세요(1:EN/2:FR/3:KR)"))
# greet(h)

# 문제2
# def concate(s1, s2):
#     return s1 + s2
# str1 = input("1'st 문장입력:")
# str2 = input("2'st 문장입력:")
# print(concate(str1, str2))

# 문제3
# def price(menue):
#     result = ""
#     if menue == 1:
#         result =  "아메리카노 2500원"
#     elif menue == 2:
#         result = "카페라떼 3000원"
#     elif menue == 3:
#         result = "바닐라라떼 3000원"
#     else:
#         result = "지원하지 않습니다."
#     return result
#
# menue = int(input("메뉴선택(1:아메리카노/2:카페라떼/3:바닐라라떼)"))
# print(price(menue))


# 문제4
# def check_grade(score):
#     check = bool
#     grade = ""
#
#     try:
#         float(score)
#         check = True
#     except ValueError:
#         check = False
#
#     if check:
#         score = float(score)
#         if 0.9 <= score < 1:
#             grade = "A"
#         elif 0.8 <= score < 0.9:
#             grade = "B"
#         elif 0.7 <= score < 0.8:
#             grade = "C"
#         elif 0.6 <= score < 0.7:
#             grade = "D"
#         elif 0 <= score < 0.6:
#             grade = "F"
#         else:
#             grade = "Bad score"
#     else:
#         grade = "Bad score"
#
#     return grade

def check_grade(score):
    grade = ""

    if 0 < score <1:
        score = float(score)
        if 0.9 <= score < 1:
            grade = "A"
        elif 0.8 <= score < 0.9:
            grade = "B"
        elif 0.7 <= score < 0.8:
            grade = "C"
        elif 0.6 <= score < 0.7:
            grade = "D"
        elif 0 <= score < 0.6:
            grade = "F"
        else:
            grade = "Bad score"

grade = input("Enter score : ")
print(check_grade(grade))
