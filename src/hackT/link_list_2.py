""" Day 24: More Linked Lists """

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def getAsList(self, head):
        res = []

        current = head
        while current:
            res.append(current.data)
            current = current.next

        return res


    def removeDuplicates(self, head):
        if not head:
           return head 

        curr = head.next
        headData = head.data
        prev = head

        while curr is not None:
            if headData == curr.data:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next


        if head.next is not None:
            self.removeDuplicates(head.next)

        return head

