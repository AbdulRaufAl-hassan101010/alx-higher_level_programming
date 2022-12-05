#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # validate if the list id is not negative or >= the list length
    if idx < 0 or idx >= len(my_list):
        return my_list

    # replace list item
    my_list[idx] = element
    return my_list
