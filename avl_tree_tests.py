import unittest
import avl_tree

class NodeTests(unittest.TestCase):
    def setUp(self):
        self.node = avl_tree.Node(1)

    def testCreation(self):
        self.assertIsNotNone(self.node)

class TreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = avl_tree.Avl_Tree()

    def testCreation(self):
        self.assertIsNotNone(self.tree)

    def testInsert(self):
        self.assertTrue(len(self.tree) == 0)
        self.tree.insert(1)
        self.assertTrue(len(self.tree) == 1)
        self.tree.insert(2)
        self.assertEqual(len(self.tree), 2)

    def testBalancedInsert(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(3)
        self.assertEqual(self.tree.root.cargo, 4)

if __name__ == '__main__':
    unittest.main()
