# Python print() width %formatting
print("%5d %7d %07d %10s %7.3f" % (123, 456, 678, "Python", 123.456789))
print("%5d %7d %07d %-10s %10.6f" % (12, 34, 5, "Python", 123.456789))

# Python print() with .format()
print("{0:5d} {1:7d} {2:07d} {3:10s} {4:7.3f}".format(123, 456, 678, "Python", 123.456789))
print("{0:5d} {1:7d} {2:07d} {3:<10s} {4:10.6f}".format(12, 34, 5, "Python", 123.456789))
print("{0:5d} {1:7d} {2:07d} {3:^10s} {4:10.6f}".format(12, 34, 5, "Python", 123.4567))
print("{0:5d} {1:7d} {2:07d} {3:>10s} {4:10.6f}".format(12, 34, 5, "Python", 123.4567))
print("Long integer with comma at each 1000 unit : ", format(123456789, ',d'))