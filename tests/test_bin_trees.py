""" Day 22: Binary Search Trees test """

from hackT import bin_trees

def test_1():
    a = [3, 5, 2, 1, 4, 6, 7]

    myTree = bin_trees.Solution()
    root=None
    for i in a:
        data = i
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)

    assert height == 3



