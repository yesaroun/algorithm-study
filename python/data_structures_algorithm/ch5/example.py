v = None
# None은 불변 객체이다.
# None이 있으면 not쓰지 말것
# 객체로 판단하는 것은 is로 판단하기?
if not v:
    print("Here1")
# 0은 False이므로

if v is None:
    print("Here2")

v = 0
if not v:
    print("Here3")

if v is None:
    print("Here4")

str_ = ""
if not str_:
    print("Here5")

if str_ is None:
    print("Here6")