#!/usr/bin/python3
a = [1, 2]
print(id(a))
b = [3, 4]
a += b
print(a)
print(id(a))
