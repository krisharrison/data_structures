#Binary Tree Implementation

#Nodes have three components: value, pointer to the left child, pointer to the right child
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


#BinaryTree handles binary tree operations
#Every Binary Tree is instantiated with the an initial node as the root
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.peorder_print(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

#Start is updated on every single recursive call
#Traversal is a string that prints out to the screen and updated on every recursive call
    def peorder_print(self, start, traversal):
        #Pre-order Traversal - Root-Left-Right
        if start:
            #At every recursive call print out the current node value and concatenate to start string)
            traversal += (str(start.value) + "-")
            #recursively calling preorder print with left subtree as the first argument
            #Passing the traversal string as the second to keep track of nodes visited
            traversal = self.peorder_print(start.left, traversal)
            #Pass the right child of the current node as the first argument
            traversal = self.peorder_print(start.right, traversal)
        return traversal


#Root of the tree
tree = BinaryTree(1)
#Left child of root
tree.root.left = Node(2)
#Right child of root
tree.root.right = Node(3)
#Left child of 2
tree.root.left.left = Node(4)
#Right child of 2
tree.root.left.right = Node(5)
#Right child of 3
tree.root.right.left = Node(6)
#Left child of 3
tree.root.right.right = Node(7)


print(tree.print_tree("preorder"))
