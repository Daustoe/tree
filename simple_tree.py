__author__ = 'Clayton Powell'

class Node(object):
    def __init__(self, data, parent):
        self.right = None
        self.left = None
        self.cargo = data
        self.parent = parent

    def insert(self, data):
        if self.cargo > data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Node(data, self)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data, self)

    def search_smallest(self):
        if self.left is None:
            self.parent.remove_me(self)
            return self.cargo
        else:
            return self.left.search_smallest()

    def remove(self, data):
        if self.cargo == data:  # remove me!
            if self.left is None and self.right is None:  # leaf
                self.parent.remove_me(self)
            elif self.left is None:
                self.parent.link(self, self.right)
            elif self.right is None:
                self.parent.link(self, self.left)
            else:
                self.cargo = self.right.search_smallest()


        elif self.cargo > data and self.left is not None:
            self.left.remove(data)
        elif self.right is not None:
            self.right.remove(data)

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
            return left + right  1

    def search(self, data):
        left = False
        right = False
        if self.cargo == data:  # Found the data!
            return True
        else:                   # Check children
            if self.left is not None:
                left = self.left.search(data)
            if self.right is not None:
                right = self.right.search(data)
            return left or right

    def remove_me(self, node):
        if self.left is node:
            self.left = None
        else:
            self.right = None

    def link(self, node, new_node):
        if self.left is node:
            self.left = new_node
        else:
            self.right = new_node

    def depth(self):
        left = []
        right = []
        if self.left is not None:
            left = self.left.depth()
        if self.right is not None:
            right = self.right.depth()
        return left + [self.cargo] + right



class Tree(object):
    """
    Ordered binary tree implementation.
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not hasattr(data, '__iter__'):
            data = [data]
        for each in data:
            if self.root is None:
                self.root = Node(each, self)
            else:
                self.root.insert(each)

    def remove_me(self, node):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    def search(self, data):
        if self.root is None:
            return False
        else:
            return self.root.search(data)

    def remove(self, data):
        if self.root is not None:
            self.root.remove(data)

    def depth(self):
        return self.root.depth()
