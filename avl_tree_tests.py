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

    def test_balanced_insert(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.assertEqual(self.tree.root.cargo, 5)
        self.tree.insert(3)
        self.assertEqual(self.tree.root.cargo, 4)
        self.assertEqual(self.tree.root.left.cargo, 3)
        self.assertEqual(self.tree.root.right.cargo, 5)
        self.assertListEqual([3, 4, 5], self.tree.traverse('cargo'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))
        self.tree.insert(1)
        self.assertListEqual([1, 3, 4, 5], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 1, 0], self.tree.traverse('balance'))
        self.tree.insert(0)
        self.assertEqual(self.tree.root.cargo, 3)
        self.assertListEqual([0, 1, 3, 4, 5], self.tree.traverse('cargo'))
        self.assertListEqual([0, 0, 0, 1, 0], self.tree.traverse('balance'))
        print self.tree.traverse('balance')
        print self.tree.traverse('cargo')

if __name__ == '__main__':
    unittest.main()
