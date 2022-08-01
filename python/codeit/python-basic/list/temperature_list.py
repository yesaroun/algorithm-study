
def fahrenheit_to_celsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9


fahrenheit_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(fahrenheit_list))

i = 0
celsius_list = []

while i < len(fahrenheit_list):
    celsius_list.append(round(fahrenheit_to_celsius(fahrenheit_list[i]), 1))
    i += 1

print("섭씨 온도 리스트" + str(celsius_list))