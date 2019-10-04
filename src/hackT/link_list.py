""" Day 15: Linked List """ 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def getAsList(self,head):
        r = []
        current = head
        while current:
            r.append(current.data)
            current = current.next

        return r

    def insert(self,head,data): 
    #Complete this method
        node = Node(data)

        if head == None:
            return node
        
        current = head
        while current.next:
            current = current.next

        current.next = node

        return head

