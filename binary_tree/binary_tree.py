# -*- coding: utf-8 -*-
'实现二叉树及几种遍历方式'

class Node(object):
    '节点实现'
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree(object):
    '二叉树实现'
    def __init__(self, node):
        if not isinstance(node, Node):
            raise TypeError("error input param")
        self.root = node

    def add_node(self, node):
        if not isinstance(node, Node):
            raise TypeError("error input param")

        root_node = self.root
        while True:
            if node.data < root_node.data:
                # 向左边移动
                if root_node.left is None:
                    root_node.left = node
                    break
                else:
                    root_node = root_node.left
            else:
                # 向右边移动
                if root_node.right is None:
                    root_node.right = node
                    break
                else:
                    root_node = root_node.right

    @classmethod
    def front_display_list(cls, root):
        '先序遍历'
        if root is None:
            return []
        left_list = cls.front_display_list(root.left)
        right_list = cls.front_display_list(root.right)
        return [root.data] + left_list + right_list
    
    @classmethod
    def mid_display_list(cls, root):
        '中序遍历'
        if root is None:
            return []
        left_list = cls.mid_display_list(root.left)
        right_list = cls.mid_display_list(root.right)
        return left_list + [root.data] + right_list
    
    @classmethod
    def last_display_list(cls, root):
        '后序遍历'
        if root is None:
            return []
        left_list = cls.last_display_list(root.left)
        right_list = cls.last_display_list(root.right)
        return left_list + right_list + [root.data]
    
    @classmethod
    def floor_display_list(cls, root):
        '层次遍历'
        from collections import deque
        q = deque()
        lst = []
        if root is None:
            return lst
        q.append(root)
        while q:
            node = q.popleft()
            lst.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return lst

node = Node(0)
node1 = Node(1)
root = Node(2)
node3 = Node(3)
node4 = Node(4)
tree = BinaryTree(root)
tree.add_node(node)
tree.add_node(node1)
tree.add_node(node3)
tree.add_node(node4)
print tree.front_display_list(root)
print tree.mid_display_list(root)
print tree.last_display_list(root)
print tree.floor_display_list(root)