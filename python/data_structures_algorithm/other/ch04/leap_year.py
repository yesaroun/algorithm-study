# if-else statements to check leap year

year = int(input('year : '))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("Year (%d) is a leap year"%(year))
else:
    print("Year (%d) is not a leap year"%(year))