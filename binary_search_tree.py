#BINARY SEARCH TREE
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #Check if root node is None
        if self.root is None:
            #Set root of tree
            self.root = Node(data)
        else:
            #Insert new node if there is at least one node in the tree, starting at the root
            self._insert(data, self.root)

    #Helper method to determine where the new node will be inserted
    def _insert(self, data, cur_node):
        #Check if data is less than current node
        if data < cur_node.data:
            if cur_node.left is None:
                #If there is no left child node insert node as left child as current node
                cur_node.left = Node(data)
            else:
                #Navigate to left child of current node
                self._insert(data, cur_node.left)
        #Check if data is greater than current node
        elif data > cur_node.data:
            #Check if right child of current node is None
            if cur_node.right is None:
                #Insert node as right child of current node if None
                cur_node.right = Node(data)
            else:
                #Navigate to the right child node
                self._insert(data, cur_node.right)
        else:
            print("Value is already present in tree")
    
    def find(self, data):
        #If there is at least one node in the tree
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                #If found
                return True
            #If not found
            return False
        else:
            #If tree is empty
            return None

    #Helper function for find
    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)

        if data == cur_node.data:
            return True


bst = BST()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
