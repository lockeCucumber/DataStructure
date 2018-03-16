# -*- coding: utf-8 -*-
'''展示节点及节点单链表的实现'''
import copy

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return 'node with {}'.format(self.value)

class NodeList(object):
    def __init__(self, node):
        self.head = node
        tmp = copy.deepcopy(node)
        while tmp.next:
            tmp = tmp.next
        self.tail = tmp

    def add_node(self, node):
        self.tail.next = node
        self.tail = node

    def del_node(self, index):
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
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def display(self):
        link = " --> "
        node = self.head
        s = str(self.head.value)
        while node.next:
            s += link + str(node.next.value)
            node = node.next
        print s 

    def find_node(self, index):
        if index > self.length() or index < 0:
            raise IndexError("index out of range")
        node = self.head
        while index > 0:
            node = node.next
            index -= 1
        return node

def reverse_recursion(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursion(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse(head):
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