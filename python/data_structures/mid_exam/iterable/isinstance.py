from collections.abc import Iterable

list_ = [1, 2, 3]
print(type(list_), isinstance(list_, Iterable))
tuple_ = (1, 2, 3)
print(type(tuple_), isinstance(tuple_, Iterable))
dict_ = {1: "hello", 2: "world"}
print(type(dict_), isinstance(dict_, Iterable))
set_ = {1, 2, 3}
print(type(set_), isinstance(set_, Iterable))
str_ = "hello"
print(type(str_), isinstance(str_, Iterable))
int_ = 10
print(type(int_), isinstance(int_, Iterable))

class Foo:
    pass

foo = Foo()
print(type(foo), isinstance(foo, Iterable))
'''
<class_ 'list'> True
<class_ 'tuple'> True
<class_ 'dict'> True
<class_ 'set'> True
<class_ 'str'> True
<class_ 'int'> False
<class_ '__main__.Foo'> False
'''