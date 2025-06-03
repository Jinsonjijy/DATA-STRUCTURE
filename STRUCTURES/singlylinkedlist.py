class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def inseratbegin(self,data):
        new_node=Node(data)
        new_node.next=self.head
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
    def insertatend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node
    def update_node(self,data,index):
        position=0
        current_node=self.head
        while current_node is not None and position!=index:
            position+=1
            current_node=current_node.next
        if current_node is not None:
            current_node.val=data
        else:
            print("index out of bound")
    def remove_first(self):
        if self.head is None:
            return
        self.head=self.head.next
    def remove_end(self):
        if self.head is  None:
            return
        current_node=self.head
        while current_node.next and current_node.next.next:
            current_node=current_node.next
        current_node.next=None
    def remove_index(self,index):
        position=0
        current_node=self.head
        while current_node is not None and position+1!=index:
            current_node=current_node.next
            position+=1
        if current_node.next is not None:
            current_node.next=current_node.next.next
        else:
            print("index out of bound")
    def traversal(self):
        current_node=self.head
        while current_node is not None:

            print(current_node.val,end="->")
            current_node=current_node.next
        print("None")

l=linkedlist()
l.inseratbegin(23)
l.inseratbegin(24)
l.inseratbegin(26)
l.inseratbegin(27)
l.inseratbegin(28)
l.insertatindex(34,0)
l.traversal()
l.remove_first()
l.traversal()