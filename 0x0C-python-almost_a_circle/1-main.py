#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    r = Rectangle(2, 4, 0, 0, 5)
    r.update(90, 2, 5, 6, 8)
    print(r.to_dictionary())
