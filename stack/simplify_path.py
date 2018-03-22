# -*- coding: utf-8 -*-
'简化路径'

# Given an absolute path for a file (Unix-style), simplify it.
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

def simplify_path(path):
    path_lst = [item for item in path.split('/') if item not in ('.', '')]
    stack = []
    for item in path_lst:
        if stack and item == '..':
            stack.pop()
        else:
            stack.append(item)
    return '/' + '/'.join(stack)

path = "/a/./b/../..///c/"
print simplify_path(path)
