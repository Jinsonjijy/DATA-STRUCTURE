class Tree:
    def __init__(self,data):
        self.data=data
        self.left_node=None
        self.right_node=None

if __name__ == "__main__":
    root=Tree(input("enter the root node"))
    nodeA=Tree(input("enter the left subnode"))
    nodeB=Tree(input("enter right sub node"))
    root.left_node=nodeA
    root.right_node=nodeB
    print("root.right.data:", root.right_node.data)