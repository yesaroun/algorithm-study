class Barebone:
    pass

bb = Barebone()

print(type(bb))
#--==>> <class '__main__.Barebone'>

bb_01 = Barebone()
print(id(bb_01))
#--==>> 4376379152

bb_02 = Barebone()
print(id(bb_02))
#--==>> 4376376656

bb_03 = bb_01

print(bb_01 is bb_02)
#--==>> False
print(bb_01 is bb_03)
#--==>> True