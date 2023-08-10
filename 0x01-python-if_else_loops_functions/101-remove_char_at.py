#!/usr/bin/python3
def remove_char_at(str, n):
    x = len(str)
    if n >= x or n < 0:
        return str
    else:
        ptr = ""
        for i in range(0, x):
            if i != n:
                ptr += str[i]
    return ptr
