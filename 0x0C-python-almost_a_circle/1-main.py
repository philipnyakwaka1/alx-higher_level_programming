#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)
    print(r1.width)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 1, 5, 12)
    print(r3.id)

    r4 = Rectangle()
    print("r4: ", r4.width)