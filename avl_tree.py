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
            else:
                self.left = Node(data)
                self.left.parent = self
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                self.right.parent = self
        self.calculate_height()
        self.rebalance()
        self.rotation_check()

    def is_leaf(self):
        return self.height == 0

    def rebalance(self):
        if self.is_leaf():
            self.balance = 0
        else:
            self.balance = (self.left.height + 1 if self.left else 0) - (self.right.height + 1 if self.right else 0)

    def rotation_check(self):
        if self.balance == 2:
            if self.left and self.left.balance == -1:
                self.left.rotate_left()
            self.rotate_right()
        elif self.balance == -2:
            if self.right and self.right.balance == 1:
                self.right.rotate_right()
            self.rotate_left()

    def point_to(self, node):
        if node.cargo < self.cargo:
            self.left = node
        else:
            self.right = node

    def rotate_left(self):
        cargo = self.right.cargo
        self.right.cargo = self.cargo
        self.cargo = cargo
        rotato = self.right
        self.right = rotato.right
        rotato.right = rotato.left
        rotato.left = self.left
        self.left = rotato
        rotato.calculate_height()
        rotato.rebalance()
        self.calculate_height()
        self.rebalance()

    def rotate_right(self):
        cargo = self.left.cargo
        self.left.cargo = self.cargo
        self.cargo = cargo
        rotato = self.left
        self.left = rotato.left
        rotato.left = rotato.right
        rotato.right = self.right
        self.right = rotato
        rotato.calculate_height()
        rotato.rebalance()
        self.calculate_height()
        self.rebalance()

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

    def remove_me(self, node):
        if node.cargo < self.cargo:
            self.left = None
        else:
            self.right = None

    def is_limb(self):
        if not self.is_leaf() and (self.left is None or self.right is None):
            return True
        else:
            return False

    def take_leftmost(self):
        if self.left is None:
            return self.cargo, True, self.right
        else:
            data, remove, branch = self.left.take_leftmost()
            if remove:
                self.left = branch
            self.calculate_height()
            self.rebalance()
            return data, False, None

    def remove(self, data):
        if self.cargo == data:
            if self.is_leaf():
                self.parent.remove_me(self)
                return True
            elif self.is_limb():
                self.parent.point_to(self.right)
                return True
            else:
                self.cargo, remove, branch = self.right.take_leftmost()
                if remove:
                    self.right = branch
                self.calculate_height()
                self.rebalance()
                return True
        elif self.left and data < self.cargo:
            return self.left.remove(data)
        elif self.right and data >= self.cargo:
            return self.right.remove(data)
        else:
            return False


class AvlTree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        return 'AvlTree'

    def point_to(self, node):
        self.root = node

    def remove_me(self, node):
        self.root = None

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

    def remove(self, data):
        if self.root:
            if self.root.remove(data):
                self.count -= 1