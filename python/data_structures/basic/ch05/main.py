# list []
# tuple ()
# dictionary {키:값}
# set {}

# 리스트 슬라이싱 : 리스트명[시작:끝] : 시작요소부터 (끝-1)인덱스 요소까지 선택

a = [10, 20]

# append(x) : 리스트 맨 마지막에 x의 값을 추가한다
a.append(30)
# insert(index, x) : 리스트의 위치(index)에 x값을 넣는다
a.insert(1, 15)
a.append([40, 50])  # 리스트에 리스톧 추가 가능
print(a)            #--==>> [10, 15, 20, 30, [40, 50]]
# pop() : 리스트 맨 뒤의 값을 빼내고, 빼낸 항목은 삭제한다.
print(a.pop())      #--==>> [40, 50]
# pop(index) : 리스트에서 index가 가리키는 값을 빼내고, 빼낸 항목은 삭제한다.
a.pop(1)
# remove(x) : 리스트에서 x를 삭제하는 함수이다(단, x의 값이 중복이면 첫 번째만 삭제한다.)
a.remove(20)
# sort() : 오름차순 정렬, sort(reverse=True) : 내림차순
a.sort(reverse=True)
a.sort()
print(a)            #--==>> [10, 30]
# count() : 리스트에서 찾을 값의 개수 세기
print(a.count(10))  #--==>> 1
# index() : 리스트에서 값의 위치 반환
print(a.index(10))  #--==>> 0
# reverse() : 리스트를 그대로 거꾸로 뒤집는다
a.reverse()
print(a)            #--==>> [30, 10]

# 튜플 : 한번 저장된 값은 수정할 수 없는 자료형, 저장된 데이터를 변경시킬 수 없다는 점만
# 제외하면 리스트와 완전히 동일

# 딕셔너리 요소에 접근하기
menu = {"김밥":2000, "라면":3000}
print(menu["김밥"])   #--==>> 2000
# keys() : 키들만 모아서 반환
print(menu.keys())      #--==>> dict_keys(['김밥', '라면'])
# values() : 값들만 모아서 반환
print(menu.values())    #--==>> dict_values([2000, 3000])
# items() : key와 value의 쌍을 튜플로 묶은 값을 반환
print(menu.items())     #--==>> dict_items([('김밥', 2000), ('라면', 3000)])
# get() : 딕셔터리의 키로 값을 추출하는 기능으로 딕셔너리[키]와 같은 기능을 수행하지만,
# 키가 존재하지 않을 경우에는 KeyError를 발생시키지 않는다
print(menu.get("초밥"))   #--==>> None
# del(), pop() : 딕셔너리 요소 삭제하기
menu.pop("김밥")
del(menu["라면"])
print(menu)             #--==>> {}

# 세트 : 중복을 헝요하지 않는 컬렉션 자료형, 순서가 없기 때문에
# 인덱싱으로 값을 얻을 수 없다.
# 세트 연산
b = {10, 20, 30}
c = {20, 40}
print(b & c)        # 교집합 : {20}
print(b.intersection(c))    # 교집합 : {20}
print(b | c)        # 합집합 : {20, 40, 10, 30}
print(b.union(c))   # 합집합 : {20, 40, 10, 30}
print(b - c)        # 차집합 : {10, 30}
print(b.difference(c))      # 차집합 : {10, 30}
# add() : 값 1개 추가
b.add(40)
# update() : 값 여러 개 추가
b.update([50, 60])
# remove() : 특정 값 삭제
b.remove(10)
print(b)
#--==>> {40, 50, 20, 60, 30}

# 헷갈림!!!
score = list(range(1, 6))
print(score)        #--==>> [1, 2, 3, 4, 5]
print(score[2])     #--==>> 3
print(score[:3])    #--==>> [1, 2, 3]
print(score[-1])    #--==>> 5
print(score[2:4])   #--==>> [3, 4]
print(score[3:])    #--==>> [4, 5]

A = {1, 2, 3}
B = {3, 4, 5, 5}
print(A | B)        #--==>> {1, 2, 3, 4, 5}
print(A & B)        #--==>> {3}
print(A - B)        #--==>> {1, 2}

num = [50, 30, 70, 40]
num.remove(30)
num.sort()
print(num)      #--==>> [40, 50, 70]

people = {100:"yang", 200:"jang", 300:"0"}
print(people.get(200))      #--==>> jang
del(people[100])
print(people)               #--==>> {200: 'jang', 300: '0'}