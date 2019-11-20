# -*- coding: utf-8 -*-
'实现对无序数字列表的排序'

def merge_help(a_list, b_list):
    res = []
    while a_list and b_list:
        num = min(a_list[0], b_list[0])
        res.append(num)
        if num == a_list[0]:
            del a_list[0]
        else:
            del b_list[0]
    res.extend(a_list)
    res.extend(b_list)
    return res

def merge_sort(num_list):
    '归并排序'
    length = len(num_list)
    if length < 2:
        return num_list
    
    n = length / 2
    a_list = merge_sort(num_list[:n])
    b_list = merge_sort(num_list[n:])
    return merge_help(a_list, b_list)

def bubble_sort(num_list):
    '冒泡排序'
    length = len(num_list)
    for i in xrange(length-1):
        for j in xrange(i+1, length):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list

def insert_sort(num_list):
    '插入排序'
    
    for i in xrange(1, len(num_list)): 
        for j in xrange(i, 0, -1):
            if num_list[j] < num_list[j-1]:
                num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
            else:
                break
    return num_list


num_list = [3, 1, 34, 5, 0, 9]
print merge_sort(num_list)

# 执行完后，num_list本身就有序了，因为是可变对象作参数，实际上是引用传递参数
print bubble_sort(num_list) 

print insert_sort(num_list)

