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
        self.assertListEqual([9, 14, 50], self.tree.traverse('cargo'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.tree.insert(67)
        self.assertListEqual([9, 14, 50, 67], self.tree.traverse('cargo'))
        self.assertListEqual([0, -1, -1, 0], self.tree.traverse('balance'))
        self.assertListEqual([0, 2, 1, 0], self.tree.traverse('height'))
        self.tree.insert(17)
        self.assertListEqual([9, 14, 17, 50, 67], self.tree.traverse('cargo'))
        self.assertListEqual([0, -1, 0, 0, 0], self.tree.traverse('balance'))
        self.assertListEqual([0, 2, 0, 1, 0], self.tree.traverse('height'))
        self.tree.insert(72)
        self.assertListEqual([9, 14, 17, 50, 67, 72], self.tree.traverse('cargo'))
        self.assertListEqual([0, 1, 0, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([0, 0, 0, 0, -1, 0], self.tree.traverse('balance'))
        self.tree.insert(12)
        self.assertListEqual([9, 12, 14, 17, 50, 67, 72], self.tree.traverse('cargo'))
        self.assertListEqual([1, 0, 2, 0, 3, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([-1, 0, 1, 0, 1, -1, 0], self.tree.traverse('balance'))
        self.tree.insert(54)
        self.assertListEqual([9, 12, 14, 17, 50, 54, 67, 72], self.tree.traverse('cargo'))
        self.assertListEqual([1, 0, 2, 0, 3, 0, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([-1, 0, 1, 0, 1, 0, 0, 0], self.tree.traverse('balance'))
        self.tree.insert(76)
        self.assertListEqual([9, 12, 14, 17, 50, 54, 67, 72, 76], self.tree.traverse('cargo'))
        self.assertListEqual([1, 0, 2, 0, 3, 0, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([-1, 0, 1, 0, 0, 0, -1, -1, 0], self.tree.traverse('balance'))
        self.tree.insert(23)
        self.assertListEqual([9, 12, 14, 17, 23, 50, 54, 67, 72, 76], self.tree.traverse('cargo'))
        self.assertListEqual([1, 0, 2, 1, 0, 3, 0, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([-1, 0, 0, -1, 0, 0, 0, -1, -1, 0], self.tree.traverse('balance'))
        self.tree.insert(19)
        self.assertListEqual([9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76], self.tree.traverse('cargo'))
        self.assertListEqual([1, 0, 2, 0, 1, 0, 3, 0, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([-1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0], self.tree.traverse('balance'))
        self.assertEqual(50, self.tree.root.cargo)

    def test_simple_removal_leaf(self):
        self.tree.insert(1)
        self.tree.remove(1)
        self.assertEqual(len(self.tree), 0)
        self.assertEqual(self.tree.root, None)

    def test_removal_leaf(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.assertListEqual([-1, 0], self.tree.traverse('balance'))
        self.tree.remove(2)
        self.assertEqual(len(self.tree), 1)
        self.assertListEqual([0], self.tree.traverse('balance'))
        self.assertEqual(self.tree.root.cargo, 1)
        self.assertEqual(self.tree.root.right, None)

    def test_removal_limb(self):
        self.tree.insert(1)
        self.tree.insert(2)
        self.tree.remove(1)
        self.assertEqual(len(self.tree), 1)
        self.assertEqual(self.tree.root.cargo, 2)

    def test_removal_root(self):
        self.tree.insert(3)
        self.tree.insert(4)
        self.tree.insert(2)
        self.assertEqual(len(self.tree), 3)
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))
        self.tree.remove(3)
        self.assertEqual(len(self.tree), 2)
        self.assertListEqual([2, 4], self.tree.traverse('cargo'))
        self.assertNotEqual(self.tree.root.cargo, 3)

    def test_removal_complex(self):
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
        self.tree.remove(17)
        self.assertListEqual([9, 12, 14, 19, 23, 50, 54, 67, 72, 76], self.tree.traverse('cargo'))
        self.assertListEqual([1, 0, 2, 1, 0, 3, 0, 2, 1, 0], self.tree.traverse('height'))
        self.assertListEqual([-1, 0, 0, -1, 0, 0, 0, -1, -1, 0], self.tree.traverse('balance'))
        self.tree.remove(54)
        self.assertListEqual([9, 12, 14, 19, 23, 50, 67, 72, 76], self.tree.traverse('cargo'))
        self.assertListEqual([-1, 0, 0, -1, 0, 1, 0, 0, 0], self.tree.traverse('balance'))
        self.assertListEqual([1, 0, 2, 1, 0, 3, 0, 1, 0], self.tree.traverse('height'))
        self.tree.remove(72)
        self.assertListEqual([9, 12, 14, 19, 23, 50, 67, 76], self.tree.traverse('cargo'))
        self.assertListEqual([-1, 0, 0, -1, 0, 1, 0, 1], self.tree.traverse('balance'))
        self.assertListEqual([1, 0, 2, 1, 0, 3, 0, 1], self.tree.traverse('height'))
        self.tree.remove(14)
        self.assertListEqual([9, 12, 19, 23, 50, 67, 76], self.tree.traverse('cargo'))
        self.assertListEqual([-1, 0, 1, 0, 1, 0, 1], self.tree.traverse('balance'))
        self.assertListEqual([1, 0, 2, 0, 3, 0, 1], self.tree.traverse('height'))
        self.tree.remove(76)
        self.assertListEqual([9, 12, 19, 23, 50, 67], self.tree.traverse('cargo'))
        self.assertListEqual([-1, 0, 0, 0, 0, 0], self.tree.traverse('balance'))
        self.assertListEqual([1, 0, 2, 0, 1, 0], self.tree.traverse('height'))
        self.tree.remove(9)
        self.assertListEqual([12, 19, 23, 50, 67], self.tree.traverse('cargo'))
        self.assertListEqual([0, -1, 0, 0, 0], self.tree.traverse('balance'))
        self.assertListEqual([0, 2, 0, 1, 0], self.tree.traverse('height'))
        self.tree.remove(12)
        self.assertListEqual([19, 23, 50, 67], self.tree.traverse('cargo'))
        self.assertListEqual([-1, 0, 1, 0], self.tree.traverse('balance'))
        self.assertListEqual([1, 0, 2, 0], self.tree.traverse('height'))
        self.tree.remove(50)
        print self.tree
        self.assertListEqual([19, 23, 67], self.tree.traverse('cargo'))
        self.assertListEqual([0, 0, 0], self.tree.traverse('balance'))
        self.assertListEqual([0, 1, 0], self.tree.traverse('height'))



if __name__ == '__main__':
    unittest.main()