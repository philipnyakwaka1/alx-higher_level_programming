#!/usr/bin/python3
n = 1
for i in range(ord('z'), ord('a') - 1, -1):
    if n % 2 == 0:
        i -= 32
    print("{}".format(chr(i)), end="")
    n += 1
