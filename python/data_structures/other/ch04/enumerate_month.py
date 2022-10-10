# for-loop with enumerate()
Month_name = ["January", "February", "March", "April", "May", "June",\
              "July", "Auguest", "September", "October", "November", "December"]

# case A
for item in enumerate(Month_name):
    print(item)
print()

# case B
for item in enumerate(Month_name, 1):
    print(item)
print()

# case C
for i, item in enumerate(Month_name, 1):
    print("%2d" %i, item)
print()

#--==>>
'''
(0, 'January')
(1, 'February')
(2, 'March')
(3, 'April')
(4, 'May')
(5, 'June')
(6, 'July')
(7, 'Auguest')
(8, 'September')
(9, 'October')
(10, 'November')
(11, 'December')

(1, 'January')
(2, 'February')
(3, 'March')
(4, 'April')
(5, 'May')
(6, 'June')
(7, 'July')
(8, 'Auguest')
(9, 'September')
(10, 'October')
(11, 'November')
(ch11, 'December')

 1 January
 2 February
 3 March
 4 April
 5 May
 6 June
 7 July
 8 Auguest
 9 September
10 October
11 November
ch11 December
'''