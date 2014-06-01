__author__ = 'Clayton Powell'


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
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

    def count(self):
        if self.left is None and self.right is None:
            return 1
        else:
            left = 0
            right = 0
            if self.left is not None:
                left = self.left.count()
            if self.right is not None:
                right = self.right.count()
            return left + right + 1


class Avl_Tree(object):
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)
