__author__ = 'Clayton Powell'

class Node(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.cargo = data

    def insert(self, data):
        if self.cargo > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data)


class Tree(object):
    """
    Ordered binary tree implementation.
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root.insert(data):
