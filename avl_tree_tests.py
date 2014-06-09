import unittest
import avl_tree
import cProfile
import pstats


class NodeTests(unittest.TestCase):
    def setUp(self):
        self.node = avl_tree.Node(1)

    def test_creation(self):
        self.assertIsNotNone(self.node)


class TreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = avl_tree.AvlTree()
        self.profile = cProfile.Profile()
        self.profile.enable()

    def tearDown(self):
        p = pstats.Stats(self.profile)
        p.strip_dirs()
        p.sort_stats('cumtime')
        p.print_stats()

    def test_creation(self):
        self.assertIsNotNone(self.tree)

    def test_insert(self):
        self.assertTrue(len(self.tree) == 0)
        self.tree.insert(1)
        self.assertTrue(len(self.tree) == 1)
        self.tree.insert(2)
        self.assertEqual(len(self.tree), 2)

    def test_right_rotation(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(3)
        self.assertEqual(4, self.tree.root.cargo)
        self.assertListEqual([3, 4, 5], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))

    def test_left_rotation(self):
        self.tree.insert(5)
        self.tree.insert(6)
        self.tree.insert(7)
        self.assertEqual(6, self.tree.root.cargo)
        self.assertListEqual([5, 6, 7], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))

    def test_left_right_rotation(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(4)
        self.assertEqual(4, self.tree.root.cargo)
        self.assertListEqual([3, 4, 5], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))

    def test_right_left_rotation(self):
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(2)
        self.assertEqual(2, self.tree.root.cargo)
        self.assertListEqual([1, 2, 3], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))

    def test_complex_tree_is_balanced(self):
        self.tree.insert(50)
        self.tree.insert(9)
        self.tree.insert(14)
        self.tree.insert(67)
        self.tree.insert(17)
        self.tree.insert(72)
        self.tree.insert(12)
        self.tree.insert(54)
        self.tree.insert(76)
        self.tree.insert(23)
        self.tree.insert(19)
        self.assertEqual(50, self.tree.root.cargo)
        self.assertListEqual([9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76], self.tree.traverse('cargo'))

    def test_removal(self):
        pass

if __name__ == '__main__':
    unittest.main()