#!/usr/bin/python3
""" 1-main """
from models.base import Base

if __name__ == "__main__":

    r1 = Base.to_json_string([{'id': 12}])
    print(r1)
    print(type(r1))
