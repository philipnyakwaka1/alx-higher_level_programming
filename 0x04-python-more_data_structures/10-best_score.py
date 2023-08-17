#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        best_score = 0
        student = ""
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                student = key
        return student
