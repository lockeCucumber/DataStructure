# -*- coding: utf-8 -*-
'实现栈stack'

class Stack(object):
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.append(x)
    
    def pop(self):
        return self.lst.pop()
    
    def top(self):
        return self.lst[-1]

    def is_empty(self):
        if self.lst:
            return False
        return True