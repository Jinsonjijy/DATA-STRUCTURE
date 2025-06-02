class singlelin:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
head=singlelin(2)
a=singlelin(3)
b=singlelin(5)
c=singlelin(6)
head.next=a
a.next=b
b.next=c
c.next=None
temp=head
while temp:
    print(temp.val,end="->")
    temp=temp.next