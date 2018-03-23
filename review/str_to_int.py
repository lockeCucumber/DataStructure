# -*- coding: utf-8 -*-
'给定字符串，改成int'

def convert_str_to_int(s):
    if s.isdigit():
        return int(s)
    else:
        raise TypeError("error input")

s = "0023023a"
print convert_str_to_int(s)