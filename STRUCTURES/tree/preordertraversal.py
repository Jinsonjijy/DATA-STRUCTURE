from simpletree import Tree
def preorder(node):
    if node is None:
        return
    print(node.data,end=",")
    preorder(node.left_node)
    preorder(node.right_node)
root=Tree(input("root node"))
node_b=Tree(input("enter the left node"))
node_a=Tree(input("enter the right node"))
root.left_node=node_b
root.right_node=node_a
preorder(root)
