#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)
    first_char = sentence[0]
    if s_len == 0:
        return (s_len, None)
    else:
        return (s_len, first_char)
