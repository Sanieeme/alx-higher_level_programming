#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    div = []
    for num in my_list:
        if (num % 2) == 0:
            div.append(True)
        else:
            div.append(False)
    return(div)
