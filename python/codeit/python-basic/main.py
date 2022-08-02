my_family = {
    'mom': 'kim',
    'dad': 'lee',
    'son': 'son',
    'daughter': 'park'
}

# 사전에 어떤 값이 있는지 목룍이 필요할때
print(my_family.values())
#--==>> dict_values(['kim', 'lee', 'son', 'park'])
print("kim" in my_family.values())
#--==>> True
print("jung" in my_family.values())
#--==>> False


for value in my_family.values():
    print(value)
#--==>>
'''
kim
lee
son
park
'''

print(my_family.keys())
#--==>> dict_keys(['mom', 'dad', 'son', 'daughter'])

for key in my_family.keys():
    print(key)
#--==>>
'''
mom
dad
son
daughter
'''

for key in my_family.keys():
    value = my_family[key]
    print(key, value)
#--==>>
'''
mom kim
dad lee
son son
daughter park
'''

for key, value in my_family.items():
    print(key, value)
#--==>>
'''
mom kim
dad lee
son son
daughter park
'''