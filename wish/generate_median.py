# -*- coding: utf-8 -*-
'制作一个生成器，输入一个数字立即返回输入记录的中位数'
import numpy as np

num_list = []
while True:
    s = raw_input()
    if s == 'exit':
        break
    if not s.isdigit():
        print "please input a num again"
        continue
    n = int(s)
    num_list.append(n)
    print np.median(num_list)
