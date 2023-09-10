#!usr/bin/python3
"""This is module for text_indentation"""


def text_indentation(text):
    """This function prints 2 new lines in text
    after the characters '.', '?' and ':'

    Args:
        text: text to print in a modified manner
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    modified_string = ""
    flag = True
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            modified_string += text[i] + '\n\n'
            flag = True
        else:
            if flag and text[i] == ' ':
                continue
            modified_string += text[i]
            flag = False
    print(modified_string, end="")
