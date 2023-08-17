#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    elif len(a_dictionary) == 1:
        for key, value in a_dictionary.items():
            return key
    else:
        best_score = 0
        student = ""
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                student = key
        return student
