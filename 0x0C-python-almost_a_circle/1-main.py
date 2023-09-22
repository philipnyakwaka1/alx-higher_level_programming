#!/usr/bin/python3
""" 1-main """
from models.base import Base

if __name__ == "__main__":
    if type(Base.to_json_string([{'id': 12}])) is str:
        print("Hey")
