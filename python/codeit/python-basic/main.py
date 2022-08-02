# 사전 (dictionary) (중괄호를 열고 닫으면 사전임)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,      # 키가 5이고 값이 25이다.
    2: 4,
    3: 9
}
print(type(my_dictionary))
#--==>> <class 'dict'>

print(my_dictionary[3])
#--==>> 9

# 새로운 쌍을 추가하고 싶을때
my_dictionary[9] = 81       # 9에 81 추가
print(my_dictionary)
#--==>> {5: 25, 2: 4, 3: 9, 9: 81}

# 리스트와 사전의 차이점
# 리스트는 인덱스가 순서대로 출력 / 리스트의 인덱스는 정수값
# 사전은 순서라는 개념이 없다. / 사전의 키는 정수형일 필요가 없다

my_family = {
    'mom': 'kim',
    'dad': 'lee',
    'son': 'son',
    'daughter': 'park'
}

print(my_family)
#--==>> {'mom': 'kim', 'dad': 'lee', 'son': 'son', 'daughter': 'park'}
print(my_family['mom'])
#--==>> kim