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

        bst.display()

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

        bst.display()

        self.assertEqual(bst.root.data, 24)
        self.assertEqual(bst.root.left.data, 12)
        self.assertEqual(bst.root.right.data, 28)
        self.assertEqual(bst.root.right.right.data, 40)
