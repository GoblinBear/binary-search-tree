import unittest

from bst import BST


class TestBST(unittest.TestCase):
    def test_insert(self):
        bst = BST()
        bst.insert(24)
        bst.insert(28)
        bst.insert(26)
        bst.insert(27)
        bst.insert(25)
        bst.insert(12)
        bst.insert(18)
        bst.insert(15)
        bst.insert(20)
        bst.insert(35)
        bst.insert(42)
        bst.insert(40)
        bst.insert(41)
        bst.insert(33)
        bst.insert(30)
        bst.insert(34)
        bst.insert(49)
        bst.insert(56)

        self.assertEqual(bst.root.data, 24)
        self.assertEqual(bst.root.left.data, 12)
        self.assertEqual(bst.root.right.data, 28)
        self.assertEqual(bst.root.right.right.data, 35)

    def test_search(self):
        bst = BST()
        bst.insert(24)
        bst.insert(28)
        bst.insert(26)
        bst.insert(27)
        bst.insert(25)
        bst.insert(12)
        bst.insert(18)
        bst.insert(15)
        bst.insert(20)
        bst.insert(35)
        bst.insert(42)
        bst.insert(40)
        bst.insert(41)
        bst.insert(33)
        bst.insert(30)
        bst.insert(34)
        bst.insert(49)
        bst.insert(56)

        self.assertIsNone(bst.search(32))
        self.assertIsNotNone(bst.search(20))
        self.assertIsNotNone(bst.search(49))

    def test_get_top_k(self):
        bst = BST()
        bst.insert(24)
        bst.insert(28)
        bst.insert(26)
        bst.insert(27)
        bst.insert(25)
        bst.insert(12)
        bst.insert(18)
        bst.insert(15)
        bst.insert(20)
        bst.insert(35)
        bst.insert(42)
        bst.insert(40)
        bst.insert(41)
        bst.insert(33)
        bst.insert(30)
        bst.insert(34)
        bst.insert(49)
        bst.insert(56)

        top3 = bst.get_top_k(3)
        top5 = bst.get_top_k(5)

        self.assertEqual(top3, [56, 49, 42])
        self.assertEqual(top5, [56, 49, 42, 41, 40])

    def test_delete(self):
        bst = BST()
        bst.insert(24)
        bst.insert(28)
        bst.insert(26)
        bst.insert(27)
        bst.insert(25)
        bst.insert(12)
        bst.insert(18)
        bst.insert(15)
        bst.insert(20)
        bst.insert(35)
        bst.insert(42)
        bst.insert(40)
        bst.insert(41)
        bst.insert(33)
        bst.insert(30)
        bst.insert(34)
        bst.insert(49)
        bst.insert(56)

        bst.delete(35)

        self.assertEqual(bst.root.data, 24)
        self.assertEqual(bst.root.left.data, 12)
        self.assertEqual(bst.root.right.data, 28)
        self.assertEqual(bst.root.right.right.data, 40)

    def test_inorder_traversal_ascending(self):
        bst = BST()
        bst.insert(24)
        bst.insert(28)
        bst.insert(26)
        bst.insert(27)
        bst.insert(25)
        bst.insert(12)
        bst.insert(18)
        bst.insert(15)
        bst.insert(20)
        bst.insert(35)
        bst.insert(42)
        bst.insert(40)
        bst.insert(41)
        bst.insert(33)
        bst.insert(30)
        bst.insert(34)
        bst.insert(49)
        bst.insert(56)

        result = bst.inorder_traversal_ascending()

        self.assertEqual(result, [12, 15, 18, 20, 24,
                                  25, 26, 27, 28, 30,
                                  33, 34, 35, 40, 41,
                                  42, 49, 56])

    def test_inorder_traversal_descending(self):
        bst = BST()
        bst.insert(24)
        bst.insert(28)
        bst.insert(26)
        bst.insert(27)
        bst.insert(25)
        bst.insert(12)
        bst.insert(18)
        bst.insert(15)
        bst.insert(20)
        bst.insert(35)
        bst.insert(42)
        bst.insert(40)
        bst.insert(41)
        bst.insert(33)
        bst.insert(30)
        bst.insert(34)
        bst.insert(49)
        bst.insert(56)

        result = bst.inorder_traversal_descending()

        self.assertEqual(result, [56, 49, 42, 41, 40,
                                  35, 34, 33, 30, 28,
                                  27, 26, 25, 24, 20,
                                  18, 15, 12])
