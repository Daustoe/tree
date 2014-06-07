import unittest
import avl_tree


class NodeTests(unittest.TestCase):
    def setUp(self):
        self.node = avl_tree.Node(1)

    def test_creation(self):
        self.assertIsNotNone(self.node)


class TreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = avl_tree.AvlTree()

    def test_creation(self):
        self.assertIsNotNone(self.tree)

    def test_insert(self):
        self.assertTrue(len(self.tree) == 0)
        self.tree.insert(1)
        self.assertTrue(len(self.tree) == 1)
        self.tree.insert(2)
        self.assertEqual(len(self.tree), 2)

    def test_insert_and_balance(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(3)
        self.assertListEqual([3, 4, 5], self.tree.traverse('cargo'))
        self.assertEqual(4, self.tree.root.cargo)
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))
        self.tree.insert(2)
        self.assertListEqual([0, 1, 2, 0], self.tree.traverse('height'))
        self.tree.insert(6)
        self.assertListEqual([2, 3, 4, 5, 6], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 1, 0, -1, 0], self.tree.traverse('balance'))
        self.tree.insert(3.5)
        self.assertListEqual([2, 3, 3.5, 4, 5, 6], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 0, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0, 0, -1, 0], self.tree.traverse('balance'))

if __name__ == '__main__':
    unittest.main()
