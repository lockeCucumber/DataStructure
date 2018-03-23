# -*- coding: utf-8 -*-
'一个斐波那契的生成器'

def generat_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

a = generat_fib()

n = 0
for i in a:
    print i
    n += 1
    if n > 10:
        break