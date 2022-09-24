scores = {'korean':80, 'math':90, 'english':80}
for item in scores.items():     # 키와 값을 함께 출력하기 위하여 items()를 사용함
    print(item, end='')
#--==>> ('korean', 80)('math', 90)('english', 80)

print('korean' in scores)
#--==>> True
print('math' not in scores)
#--==>> False

triples = {x:x*x*x for x in range(6)}
print(triples)
#--==>> {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}