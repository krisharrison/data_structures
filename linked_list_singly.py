#LINK LISTS

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # Called last node because this will eventually be pointing to the last node
        last_node = self.head
        # Next node is not node
        while last_node.next:
            # Assigned the next node in every iteraion
            # End result is that the last node of the linked list is assigned
            last_node = last_node.next

        #Head is not at the last node
        last_node.next = new_node
