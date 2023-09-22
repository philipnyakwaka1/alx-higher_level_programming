#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
my_square.my_print()
print("my_square: ", my_square)

print("--")

my_square = Square(5, (4, 1))
print("__str__: ", my_square)
