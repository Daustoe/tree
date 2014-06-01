import unittest
import simple_tree

class SimpleTree(unittest.TestCase):
    def setUp(self):
        self.tree = simple_tree.Tree()

    def testCreation(self):
        self.assertIsNotNone(self.tree)

    def testInsert(self):
        self.assertTrue(len(self.tree) == 0)
        self.tree.insert(1)
        self.assertTrue(len(self.tree) == 1)

    def testSearch(self):
        self.tree.insert(1)
        self.assertTrue(self.tree.search(1))
        self.assertFalse(self.tree.search(0))

    def testRemove(self):
        self.assertTrue(len(self.tree) == 0)
        self.tree.insert(1)
        self.assertTrue(len(self.tree) == 1)
        self.tree.remove(1)
        self.assertTrue(len(self.tree) == 0)
        self.tree.insert(2)
        self.tree.remove(1)
        self.assertTrue(len(self.tree) == 1)

    def testDepthFirst(self):
        numbers = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 200]
        self.tree.insert(numbers)
        self.assertEqual(numbers, self.tree.depth())



if __name__ == '__main__':
    unittest.main()
