# -*- coding: utf-8 -*-
'长方形矩阵，左上到右下的方式数量'

def get_unique_path_count(m, n):
    res_list = [[1]*n]*m
    for i in xrange(1, m):
        for j in xrange(1, n):
            res_list[i][j] = res_list[i-1][j] + res_list[i][j-1]
    return res_list[-1][-1]

print get_unique_path_count(3,3)
