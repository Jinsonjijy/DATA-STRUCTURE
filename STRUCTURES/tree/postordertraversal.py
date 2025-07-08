""" in this we are traversing in a way that first we recursivly travers throught the left subtree
and then it recursively traverse through the right subtee and then the rooot node that is how the post order traversal is happening
"""
from simpletree import Tree
def postorder(node):
    if node is None:
        return
    postorder(node.left_node)
    postorder(node.right_node)
    print(node.data,end=",")
root=Tree(input("enter the root node "))
node_a=Tree(input("enter the leftnode"))
node_b=Tree(input("enter the right node"))
root.left_node=node_a
root.right_node=node_b
postorder(root)