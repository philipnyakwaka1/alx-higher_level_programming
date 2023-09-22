#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
    print(r.to_dictionary())
