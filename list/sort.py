# -*- coding: utf-8 -*-
'实现对无序数字列表的排序'

def merge_sort(num_list):
    '归并排序'
    length = len(num_list)
    if length < 2:
        return num_list
    
    n = length / 2
    a_list = merge_sort(num_list[:n])
    b_list = merge_sort(num_list[n:])

    sort_num_list = []
    while a_list and b_list:
        num = min(a_list[0], b_list[0])
        if num == a_list[0]:
            del a_list[0]
        else:
            del b_list[0]
        sort_num_list.append(num)
    sort_num_list.extend(a_list)
    sort_num_list.extend(b_list)
    return sort_num_list

def bubble_sort(num_list):
    '冒泡排序'
    length = len(num_list)
    for i in xrange(length-1):
        for j in xrange(i+1, length):
            if num_list[i] > num_list[j]:
                tmp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = tmp
    return num_list


num_list = [3, 1, 34, 5, 0, 9]
print merge_sort(num_list)

print bubble_sort(num_list) 
# 执行完后，num_list本身就有序了，因为是可变对象作参数，实际上是引用传递参数

