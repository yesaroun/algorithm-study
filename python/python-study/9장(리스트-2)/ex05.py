# 문자열에 대한 리스트 함축

# 문자열의 첫 번째 문자만 가지는 리스트를 생성하는 예제
list1 = ["korea", "대한민국", "서울특별시", "한라산", "END"]
first_word = [word[0] for word in list1]
print("단어의 첫 문자 : ", first_word)
#--==>> 단어의 첫 문자 :  ['k', '대', '서', '한', 'E']

# 문자열의 마지막 번째 문자만 가지는 리스트를 생성하는 예제
list1 = ["korea", "대한민국", "서울특별시", "한라산", "END"]
last_word = [word[len(word) - 1] for word in list1]
print("단어의 끝 문자 : ", last_word)
#--==>> 단어의 끝 문자 :  ['a', '국', '시', '산', 'D']

# 문자열의 길이만 가지는 리스트를 생성하는 예제
list1 = ["korea", "대한민국", "서울특별시", "한라산", "END"]
len_word = [len(word) for word in list1]
print("단어의 길이 : ", len_word)
#--==>> 단어의 길이 :  [5, 4, 5, 3, 3]

# 상호곱(Cross Product)
colors = ["흰색", "브라운색", "검정색"]
cars = ["그랜저", "소나타", "스파크"]
colors_cars = [x + "-" + y for x in colors
                           for y in cars ]
print("색상과 차종 : ", colors_cars)
#--==>> 색상과 차종 :  ['흰색-그랜저', '흰색-소나타', '흰색-스파크', '브라운색-그랜저', '브라운색-소나타', '브라운색-스파크', '검정색-그랜저', '검정색-소나타', '검정색-스파크']