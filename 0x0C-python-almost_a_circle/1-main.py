#!/usr/bin/python3
""" 1-main """
from models.square import Square

if __name__ == "__main__":
    r = Square.create(
        **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
    print(r.to_dictionary())
