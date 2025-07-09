""" implementing the idea  of binary search tree
resource:https://blog.boot.dev/computer-science/binary-search-tree-in-python/

"""
class node:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None
    def insert(self,val):
        if not self.val:#it is when their is no value is present
            self.val=val
            return
        if self.val==val: #in this if our tree have same valule it just go to the function call
            return
        #next is if smaller value came we use recursive call to insert the value its a insertion at left side
        if val<self.val:
            if self.left: # if we have left tree we will recursively find the loc and insert in over their
                self.left.insert(val)
                return
            # if no left subtree for that we will creat a new node and insert it to that
            self.left=node(val)
            return    # it is hard you have to analyze it very accurately to get the idea
        if val>self.val: # in this the incomming value is greater the present value then we insert at the right side
            if self.right:
                self.right.insert(val)
                return # this return is taking backtracking
            self.right=node(val)
            return
    def getmin(self):#it is mainly used to get minimum value in the tree
        current=self
        while current.left is not None:
            current=current.left
        return current
    def getmax(self): # it is mainly used to get the max value in the tree
        current=self
        while current.right is not None:
            current=current.right
        return current.right
    def delet(self,val):
        if self==None:
            return self

        if self.right==None:
            return self.left
        if self.left==None:
            return self.right
        if val<self.val:
            if self.val:
                self.left=self.left.delet(val)
            return self
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exist(self,val):
        if self.val==val:
            return True
        if val<self.val:
            if self.left is None:
                return False
            self.left.exist(val)
        if val>self.val:
            if self.right is None:
                return False
            self.right.exist(val)

