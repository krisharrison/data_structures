#Binary Tree Implementation
#Three methods of depth first search

#Stack class for reverse level-order traversal of a binary tree
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


#Queue class for level-order traversal of a binary tree
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)

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
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_print(tree.root)
        elif traversal_type == "reverselevelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

#Start is the current node and updated on every single recursive call
#Traversal is a string that prints out to the screen and updated on every recursive call
    def peorder_print(self, start, traversal):
        #Pre-order Traversal - Root-Left-Right
        if start:
            #At every recursive call print out the current node value and concatenate to traversal string)
            traversal += (str(start.value) + "-")
            #recursively calling preorder print with left subtree as the first argument
            #Passing the traversal string as the second to keep track of nodes visited
            traversal = self.peorder_print(start.left, traversal)
            #Pass the right child of the current node as the first argument
            traversal = self.peorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        #Left-Root-Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        #Left-Right-Root
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

#Level order Traversal
    def level_order_print(self,start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            traversal += (str(queue.peek()) + "-")
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return traversal
    
    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
         
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal
       

#Root of the tree
#tree = BinaryTree(1)
##Left child of root
#tree.root.left = Node(2)
##Right child of root
#tree.root.right = Node(3)
##Left child of 2
#tree.root.left.left = Node(4)
##Right child of 2
#tree.root.left.right = Node(5)
##Right child of 3
#tree.root.right.left = Node(6)
##Left child of 3
#tree.root.right.right = Node(7)

#Level Order Traversal Example
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
#print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
#print(tree.print_tree("reverselevelorder"))
