#!/usr/bin/env python3
def no_c(my_string):
    if not my_string:
        return ""

    new_char = ""
    for char in my_string:
        if char != "c" and char != "C":
            new_char += char
    return new_char
