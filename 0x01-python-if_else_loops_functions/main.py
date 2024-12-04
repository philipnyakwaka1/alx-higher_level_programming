#!/usr/bin/env python3
"""Print different two digit combinations"""
for i in range(10):
    for  j in range(i + 1, 10):
        if j == 9 and i != 8:
            print('{}{}'.format(i, j),end=", ")
        else:
            if j == 9 and i == 8:
                print('{}{}'.format(i, j))
            elif j != i:
                print('{}{}'.format(i, j),end=", ")
