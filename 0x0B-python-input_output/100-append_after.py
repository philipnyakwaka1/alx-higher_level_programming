#!/usr/bin/python3
"""module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a
    file, after each line containing a specific string
    """

    my_list = []
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            my_list.append(line)
            if search_string in line:
                my_list.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(my_list)
