# -*- coding: utf-8 -*-
'''
Given four lists A, B, C, D of integer values, 
compute how many tuples (i, j, k, l) 
there are such that A[i] + B[j] + C[k] + D[l] is zero.
'''

from collections import Counter

def get_four_sum_count(A, B, C, D):
    '''
    :type :A/B/C/D list[int]
    :rtype int
    '''
    dic = Counter(a+b for a in A for b in B)
    return sum(dic[-c-d] for c in C for d in D)
