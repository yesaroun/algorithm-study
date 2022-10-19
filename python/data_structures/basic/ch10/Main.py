# 과제1
# ss = "파이썬은완전재미있어요"
#
# sslen = len(ss)
# for i in range(0, sslen):
#     if i % 2 == 0:
#         print(ss[i], end='')
#         if i == (sslen - 1):
#             pass
#         else:
#             print("#", end='')
#     else:
#         pass

# 과제2

# inStr = "<<<파<<이>>썬>>>"
# outStr = ""
# for i in range(0, len(inStr)):
#     if inStr[i] != "<" and inStr[i] != ">":
#         outStr += inStr[i]
#
# print("원래 문자열 ==> %s%s%s" % ("[", inStr, "]"))
# print("수정 문자열 ==> %s%s%s" % ("[", outStr, "]"))

# 과제3
inStr = input("문자열 입력 : ")
result_message = ""

if inStr.isdigit():
    result_message = "글자입니다."
elif inStr.isalpha():
    result_message = "숫자입니다."
elif inStr.isalnum():
    result_message = "글자+숫자입니다."
else:
    result_message = "모르겠습니다."

print(result_message)