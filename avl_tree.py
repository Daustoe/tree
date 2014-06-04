__author__ = 'Clayton Powell'


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.cargo = data
        self.balance = 0

    def insert(self, data):
        if self.cargo > data:
            self.balance += 1
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Node(data)
                self.left.parent = self
        else:
            self.balance -= 1
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data)
                self.right.parent = self
        self.check_balance()

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

    def check_balance(self):
        if self.balance == 2:  # left branch is deeper than right
            if self.left is not None and self.left.balance == -1:  # Left child is deeper on right
                self.left.rotate_left()
            self.rotate_right()
        elif self.balance == -2:  # right branch is deeper than left
            if self.right is not None and self.right.balance == 1:  # right child is deeper on the left
                self.right.rotate_right()
            self.rotate_left()

    def point_to_me(self, node):
        if node.cargo < self.cargo:
            self.left = node
        else:
            self.right = node

    def rotate_right(self):
        # need to rebalance these rotated nodes
        rotato = self.left
        self.left = rotato.right
        if self.left is not None:
            self.left.parent = self
        rotato.parent = self.parent
        if type(self.parent) is not 'AvlTree':
            self.parent.point_to_me(rotato)
        self.parent = rotato
        rotato.right = self
        print rotato.balance
        rotato.balance -= 1
        self.balance = 0

    def rotate_left(self):
        print self.balance
        rotato = self.right  # rotation potato # child node being rotated up # hot potato
        self.right = rotato.left
        rotato.parent = self.parent
        self.parent = rotato
        rotato.left = self

    def traverse(self, attribute):
        left = []
        right = []
        if self.left is not None:
            left = self.left.traverse(attribute)
        if self.right is not None:
            right = self.right.traverse(attribute)
        return left + [getattr(self, attribute)] + right


class AvlTree(object):
    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    def __str__(self):
        return 'AvlTree'

    def point_to_me(self, node):
        self.root = node

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.parent = self
        else:
            self.root.insert(data)

    def traverse(self, attribute):
        print hasattr(self.root, attribute)
        if hasattr(self.root, attribute):
            return self.root.traverse(attribute)
