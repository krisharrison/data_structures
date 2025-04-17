#Binary Tree Implementation

#Nodes have three components: value, pointer to the left child, pointer to the right child
class Node:
    def __init__(self,value):
        self.valuie = value
        self.left = None
        self.right = None


#BinaryTree handles binary tree operations
#Every Binary Tree is instantiated with the an initial node as the root
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

#Start is updated on every single recursive call
#Traversal is a string that prints out to the screen and updated on every recursive call
    def peorder_print(self, start, traversal):
        #Pre-order Traversal - Root-Left-Right
        if start:
            #At every recursive call print out the current node value and concatenate to start string)
            traversal = traversal + (str(start.value) + "-")
            #recursively calling preorder print with left subtree as the first arguement
            #Passing the traversal string as the second to keep track of nodes visited
            traversal = self.peorder_print(start.left, traversal)
            #Pass the right child of the current node as the first argument
            traversal = self.peorder_print(start.right, traversal)


#Root of the tree
tree = BinaryTree(1)
#Left child of root
tree.left = Node(2)
#Right child of root
tree.right = Node(3)
#Left child of 2
tree.root.left.left = Node(4)
#Right child of 2
tree.root.left.right = Node(5)
#Right child of 3
tree.right.left = Node(6)
#Left child of 3
tree.right.right = Node(7)
#Right child of 7
tree.root.right.right.right = Node(8)
