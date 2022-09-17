# colors 리스트의 원소와 cars리스트의 원소가 하나씩 짝지어져서 튜플이 되고
# 이 튜플이 모여서 리스트가 된다.
colors = ['white', 'silver', 'black']
cars = ['bnw5', 'sonata', 'malibu', 'sm5']
colored_cars = [(x,y) for x in colors for y in cars]
print(colored_cars)
#--==>> [('white', 'bnw5'), ('white', 'sonata'), ('white', 'malibu'), ('white', 'sm5'), ('silver', 'bnw5'), ('silver', 'sonata'), ('silver', 'malibu'), ('silver', 'sm5'), ('black', 'bnw5'), ('black', 'sonata'), ('black', 'malibu'), ('black', 'sm5')]