#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except:
        import sys
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
