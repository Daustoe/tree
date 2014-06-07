__author__ = 'Clayton Powell'


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.cargo = data
        self.balance = 0
        self.height = 0

    def insert(self, data):
        if data < self.cargo:
            if self.left:
                self.left.insert(data)
                self.calculate_height()
            else:
                self.left = Node(data)
                self.left.parent = self
                self.height = max(1, self.height)
        else:
            if self.right:
                self.right.insert(data)
                self.calculate_height()
            else:
                self.right = Node(data)
                self.right.parent = self
                self.height = max(1, self.height)
        self.calculate_balance()
        self.check_for_rotation()
        return self.height

    def is_leaf(self):
        return self.height == 0

    def calculate_balance(self):
        if self.is_leaf():
            self.balance = 0
        else:
            self.balance = (self.left.height + 1 if self.left else 0) - (self.right.height + 1 if self.right else 0)

    def check_for_rotation(self):
        if self.balance == 2:  # left branch
            if self.left and self.left.calculate_balance == -1:  # Left child is deeper on right
                self.left.rotate_left()
            self.rotate_right()
        elif self.balance == -2:  # left branch is deeper than left
            if self.right and self.right.calculate_balance == 1:  # right child is deeper on the left
                self.right.rotate_right()
            self.rotate_left()

    def point_to_me(self, node):
        if node.cargo < self.cargo:
            self.left = node
        else:
            self.right = node

    def rotate_left(self):
        print "here"
        rotato = self.left
        self.left = rotato.right
        if self.left is not None:
            self.left.parent = self
        rotato.parent = self.parent
        self.parent.point_to_me(rotato)
        self.parent = rotato
        rotato.right = self
        print rotato.balance
        rotato.balance -= 1
        self.balance = 0

    def rotate_right(self):
        # switch cargo values with self.left
        cargo = self.left.cargo
        self.left.cargo = self.cargo
        self.cargo = cargo

        # temp variable holding moving node (self.left)
        rotato = self.left
        self.left = rotato.left

        # switch moving node's right branch to be my left,
        rotato.left = rotato.right
        rotato.right = self.right
        self.right = rotato

        # handle new heights/balances
        rotato.calculate_height()
        rotato.calculate_balance()
        self.calculate_height()
        self.calculate_balance()

    def calculate_height(self):
        self.height = max(self.left.height if self.left else -1, self.right.height if self.right else -1) + 1

    def traverse(self, attribute):
        left = []
        right = []
        if self.left:
            left = self.left.traverse(attribute)
        if self.right:
            right = self.right.traverse(attribute)
        return left + [getattr(self, attribute)] + right


class AvlTree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        return 'AvlTree'

    def point_to_me(self, node):
        self.root = node

    def insert(self, data):
        if self.root:
            self.root.insert(data)
        else:
            self.root = Node(data)
            self.root.parent = self
        self.count += 1

    def traverse(self, attribute):
        if hasattr(self.root, attribute):
            return self.root.traverse(attribute)
