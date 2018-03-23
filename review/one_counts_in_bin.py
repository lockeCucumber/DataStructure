# -*- coding: utf-8 -*-
'统计一个数字的二进制形式有几个1'

def count_one(num):
    s = '{:b}'.format(num)
    s = s.replace('0', '')
    return len(s)

print count_one(8)