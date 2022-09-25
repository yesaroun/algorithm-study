dic = {"bags": 1, "books":5, "bottles":4, "coins":7, "cups":2, "pens":3}

print(sorted(dic))
# 딕셔너리 객체를 받아서 정렬된 키들의 리스트를 반환
#--==>> ['bags', 'books', 'bottles', 'coins', 'cups', 'pens']

# 딕셔너리의 값을 정렬하고 싶으면 values()메소드를 사용
print(sorted(dic.values()))
#--==>> [1, 2, 3, 4, 5, 7]

# 딕셔너리의 값에 따라서 키들을 정렬하고 싶으면 sorted()함수에 요소들을 비교할 때 사용하는 키를 지정하여야 한다.
print(sorted(dic, key=dic.__getitem__))
#--==>> ['bags', 'cups', 'pens', 'bottles', 'books', 'coins']

# keys() : 키만 출력
print(dic.keys())
#--==>> dict_keys(['bags', 'books', 'bottles', 'coins', 'cups', 'pens'])

# values() : 값을 출력
print(dic.values())
#--==>> dict_values([1, 5, 4, 7, 2, 3])