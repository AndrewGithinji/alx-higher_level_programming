#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0:
            return "None"
        if idx > my_list:
            return "None"
        else:
            print(my_list[idx])