#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = (0, 0)
    tuple_b = (0, 0)

    if tuple_a < 0:
        tuple_a = (0, 0)
    else:
        if tuple_a > 1:
            tuple_a = (1, 1)
        else:
            if tuple_b < 0:
                tuple_b = (0, 0)
            else:
                if tuple_b > 1:
                    tuple_b = (1, 1)
                    tuple_c = [tuple_a + tuple_b]
                    print(tuple_c)
