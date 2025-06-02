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
    def insertatindex(self,data,index):
        if index==0:
            self.inseratbegin(data)
            return
        position=0
        current_node=self.head
        while current_node is not None and position+1!=index:
            position+=1
            current_node=current_node.next
        if current_node is not None:
            new_node=Node(data)
            new_node.next=current_node.next
            current_node.next=new_node
            
        else:
            print("index out of bound  not found")

l=linkedlist()
l.inseratbegin(23)
