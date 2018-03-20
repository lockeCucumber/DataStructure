# -*- coding: utf-8 -*-
'''节点及单链表的实现，倒序节点的方法'''
import copy

class Node(object):
    '节点定义'
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        '重写字符形式'
        return 'node with {}'.format(self.value)

class NodeList(object):
    '单链表'
    def __init__(self, node):
        self.head = node
        tmp = copy.deepcopy(node)
        while tmp.next:
            tmp = tmp.next
        self.tail = tmp

    def add_node(self, node):
        '表尾添加节点'
        self.tail.next = node
        self.tail = node

    def del_node(self, index):
        '删除指定位置的节点'
        if index >= self.length():
            raise IndexError("index out of range")
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            return value
        node = self.head
        while index > 0:
            pre = node
            node = node.next
            index -= 1
        pre.next = node.next
        return node

    def length(self):
        '链表长度'
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def display(self):
        '展示链表'
        link = " --> "
        node = self.head
        s = str(self.head.value)
        while node.next:
            s += link + str(node.next.value)
            node = node.next
        print s 

    def find_node(self, index):
        '查找指定位置的节点'
        if index > self.length() or index < 0:
            raise IndexError("index out of range")
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node

def reverse_recursion(head):
    '倒序单链表的递归实现'
    if not head or not head.next:
        return head
    new_head = reverse_recursion(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse(head):
    '节点逐一倒序实现整个链表的倒序'
    if not head or not head.next:
        return head
    pre = None
    while head:
        next_node = head.next
        head.next = pre
        pre = head
        head = next_node
    return pre

head_node = Node(0)
head_node.next = Node(1)
head_node.next.next = Node(2)
node_list = NodeList(head_node)
node_list.display()
a = copy.deepcopy(node_list)
rev = reverse(a.head)
rev_list = NodeList(rev)
rev_list.display()
node_list.display()