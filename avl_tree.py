__author__ = 'Clayton Powell'


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.cargo = data
        self.balance = 0
        self.height = 0

    def get_representation(self):
        results = 'Node:\t\t\t' + str(self)
        results += '\n\tParent:\t\t' + str(self.parent.cargo)
        results += '\n\tLeft:\t\t' + str(self.left)
        results += '\n\tRight:\t\t' + str(self.right)
        results += '\n\tBalance:\t' + str(self.balance)
        results += '\n\tHeight:\t\t' + str(self.height) + '\n\n'
        left = ""
        right = ''
        if self.left:
            left = self.left.get_representation()
        if self.right:
            right = self.right.get_representation()
        return left + results + right

    def __str__(self):
        return str(self.cargo)

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
        self.rebalance()
        self.rotation_check()

    def is_leaf(self):
        return self.height == 0

    def rebalance(self):
        self.calculate_height()
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
        rotato = self.right
        self.link(rotato.left, 'right')
        parent = self.parent
        rotato.link(self, 'left')
        rotato.parent = parent
        parent.point_to(rotato)
        self.rebalance()
        rotato.rebalance()

    def rotate_right(self):
        rotato = self.left
        self.link(rotato.right, 'left')
        parent = self.parent
        rotato.link(self, 'right')
        rotato.parent = parent
        parent.point_to(rotato)
        self.rebalance()
        rotato.rebalance()

    def link(self, node, side):
        if side == 'left':
            self.left = node
            if node:
                node.parent = self
        else:
            self.right = node
            if node:
                node.parent = self

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
                self.rebalance()
            return data, False, None

    def limb(self):
        if self.right:
            return self.right
        else:
            return self.left

    def remove(self, data):
        if self.cargo == data:
            if self.is_leaf():
                self.parent.remove_me(self)
                return True
            elif self.is_limb():
                child = self.limb()
                self.parent.point_to(child)
                child.parent = self.parent
                return True
            else:
                self.cargo, remove, branch = self.right.take_leftmost()
                if remove:
                    self.right = branch
                self.rebalance()
                self.rotation_check()
                return True
        elif self.left and data < self.cargo:
            result = self.left.remove(data)
            if result:
                self.rebalance()
                self.rotation_check()
            return result
        elif self.right and data >= self.cargo:
            result = self.right.remove(data)
            if result:
                self.rebalance()
                self.rotation_check()
            return result
        else:
            return False

    def least(self):
        if self.left is None:
            return self.cargo
        else:
            return self.left.least()

    def greatest(self):
        if self.right is None:
            return self.cargo
        else:
            return self.right.greatest()


class AvlTree(object):
    def __init__(self, cargo=None):
        self.count = 0
        self.root = None
        if cargo:
            self.root = Node(cargo)
            self.count = 1
        self.cargo = 'head'

    def __len__(self):
        return self.count

    def __str__(self):
        return 'AvlTree:\n' + self.root.get_representation()

    def is_empty(self):
        return self.root is None

    def is_non_empty(self):
        return self.root is not None

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

    def least(self):
        if self.root:
            return self.root.least()
        else:
            return None

    def greatest(self):
        if self.root:
            return self.root.greatest()
        else:
            return None