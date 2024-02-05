#!/usr/bin/python3

def list_division(my_l_1, my_l_2, list_length):
    arr = []
    for i in range(list_length):
        try:
            res = my_l_1[i]/my_l_2[i]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            arr.append(res)
    return arr
