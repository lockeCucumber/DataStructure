#!/usr/bin/env python
# -*- coding: utf-8 -*-
'查找数字集合中逆序的对数'

def get_reverse_count(num_list):
    length = len(num_list)
    reverse_count = 0
    for i in xrange(length-1):
        for j in xrange(i+1, length):
            if num_list[i] > num_list[j]:
                reverse_count += 1

    return reverse_count

lst = [3,2,1]
print get_reverse_count(lst)