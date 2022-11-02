# 과제 1
'''
people = {100:'yang', 200:'jang', 300:'o'}
print(list(people.keys()))
print(list(people.values()))
print(list(people.items()))
print(people.get(200))
del(people[100])
print(people)
'''

# 과제 2
'''
name = ['홍일동', '홍이동', '홍삼동']
print(name)

name.append('홍사동')
print(1, name)

name.insert(2, '홍이동')
print(2, name)

print(3, name.count('홍이동'))

name.reverse()
print(4, name)

name.remove('홍일동')
print(5, name)

name.sort(reverse=True)
print(6, name)

print(7, len(name))
'''


# 과제 3
'''
addr = {}

addr['최재원']='010-1111-1234'
addr['최지윤']='010-2222-1234'
addr['김연수']='010-3333-1234'
addr['김연우']='010-4444-1234'
addr['김가현']='010-5555-1234'
addr['김혜현']='010-6666-1234'

print(addr)
print()

addr_list = list(addr.keys())
print(addr_list)

find_name = input('search name : ')
print(addr.get(find_name, 'not Found'))
'''


# 과제 4
clubA = {'kim', 'park', 'hwang'}
clubB = {'park', 'lee', 'choi'}

# 2
clubC = clubA | clubB
print(clubC)

# 3
print(clubA & clubB)

# 4
print(clubA - clubB)

# 5
print(clubB - clubA)

# 6
clubA.add('yang')

# 7
clubB.remove('lee')

# 8
print(clubA)
print(clubB)
