# -*- coding: utf-8 -*-
'蛇形打印二叉树结构'

class Node(object):
    '二叉树节点定义'
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def get_tree_list(root):
    stack = []
    stack.append(root)
    results = []
    while stack:
        node = stack.pop(0)
        results.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return results

for i in xrange(1, 9):
    locals()['node{}'.format(i)] = Node(i)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node8

tree_list = get_tree_list(node1)
tree_list = [str(i) for i in tree_list]
print tree_list
s = ''
for i in xrange(3):
    count = 2**i
    if i % 2 == 0:
        s += ' '.join(tree_list[:count]) + '\n'
    else:
        s += ' '.join(tree_list[:count][::-1]) + '\n'
    tree_list = tree_list[count:]

print s

