#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(0, 2)
    print(r1.width)
    print(r1.height)
    print(r1.x)
    print(r1.y)
    print("id:", r1.id)
