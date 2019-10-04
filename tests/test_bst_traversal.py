""" Day 23: BST Level-Order Traversal test """

from hackT import bst_traversal

def test_1():
    a = [3, 5, 4, 7, 2, 1]

    myTree = bst_traversal.Solution()
    root=None
    for i in a:
        data = i
        root=myTree.insert(root,data)

    res = myTree.levelOrder(root)

    assert res == [3, 2, 5, 1, 4, 7]


#test_1()

