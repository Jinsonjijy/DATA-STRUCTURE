class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def inseratbegin(self,data):
        new_node=Node(data)
        new_node=self.head
        self.head=new_node
l=linkedlist()
l.inseratbegin(23)
