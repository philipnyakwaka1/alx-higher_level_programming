#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

print("r1: ", r1)
print("str(r1): ", str(r1))
print("repr(r1): ", repr(r1))
print(r1.__str__)
