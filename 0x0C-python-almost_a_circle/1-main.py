#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    a = Rectangle.save_to_file([Rectangle(1, 2, 3, 6, 9)])
    b = Rectangle.load_from_file()
    print(b)
