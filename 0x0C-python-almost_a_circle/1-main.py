#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle
import io
import sys

if __name__ == "__main__":

    r = Rectangle(2, 3, 0, 0, 0)
    capture = TestRectangle_stdout.capture_stdout(r, "display")
