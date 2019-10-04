""" Day 15: Linked List test """ 

from hackT import link_list

def test_getReversedArray():
    a = [2, 3, 4, 1]

    mylist= link_list.Solution()

    head=None
    for i in a:
        data=i
        head=mylist.insert(head,data)    

    assert a == mylist.getAsList(head)
