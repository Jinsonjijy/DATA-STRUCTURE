""" in the inorder traversal we first recursive traverse the left subtree and then the root node and then the right sub
tree

"""
from simpletree import Tree
def inorder(node):
    if node is None:
        return
    inorder(node.left_node)
    print(node.data,end=",")
    inorder(node.right_node)
root=Tree(input("enter the root node"))
node_a=Tree(input("enter the lefte subtreee"))
node_b=Tree(input("enter the right subtree"))
root.left_node=node_a
root.right_node=node_b
inorder(root)