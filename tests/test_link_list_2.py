""" Day 24: More Linked Lists test """

from hackT import link_list_2

def test_1():
    a = [1, 2, 2, 3, 3, 4]

    mylist = link_list_2.Solution()

    head=None
    for i in a:
        data = i
        head = mylist.insert(head, data)    

    head = mylist.removeDuplicates(head)

    mylist.display(head)

    assert mylist.getAsList(head) == [1, 2, 3, 4]


def test_2():
    a = []

    mylist = link_list_2.Solution()

    head=None
    for i in a:
        data = i
        head = mylist.insert(head, data)    

    head = mylist.removeDuplicates(head)

    mylist.display(head)

    assert mylist.getAsList(head) == []


def test_3():
    a = [1,1,1,1,1,1,1]

    mylist = link_list_2.Solution()

    head=None
    for i in a:
        data = i
        head = mylist.insert(head, data)    

    head = mylist.removeDuplicates(head)

    assert mylist.getAsList(head) == [1]




