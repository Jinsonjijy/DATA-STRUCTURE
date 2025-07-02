class Tree:
    def __init__(self,data):
        self.data=data
        self.left_node=None
        self.right_node=None


root=Tree(input("enter the data"))
nodeA=Tree(input("enter the data"))
nodeB=Tree(input("enter the data"))
root.left_node=nodeA
root.right_node=nodeB
print("root.right.data:", root.right_node.data)