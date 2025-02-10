#LINK LISTS

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def prepend(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        #New node now points to the current head
        new_node.next = self.head
        #Head pointer not points to new node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # Called last node because this will eventually be pointing to the last node
        last_node = self.head
        # Next node is not None
        while last_node.next:
            # Assigned the next node in every iterating
            # End result is that the last node of the linked list is assigned
            last_node = last_node.next

        #Head is now at the last node
        last_node.next = new_node

    def inset_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node not in the list")
            return
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        
        #Make new node point to the current next node of previous node
        new_node.next = prev_node.next
        #The new next node of previous node is the new node
        prev_node.next = new_node

    def delete_node(self,key):
        curr_node = self.head
        
        #Use case if node is at the beginning of the list and head pointer is pointing to it
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node - None
            return
        
        #Use case if node is not first node
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            print("Node is not in the list")
            return

        #Remove current node from list
        prev_node.next = curr_node.next
        curr_node = None
        
    def del_node_pos(self,position):
        curr_node = self.head
        
        #Position is the first element
        if curr_node and position == 0:
           self.head = curr_node.next
           curr_node = None

        
        #Get node from position
        previous_node = None
        counter = 1
        while curr_node and counter != position:
            
        
            previous_node = curr_node
            curr_node = curr_node.next
            counter = counter + 1
        
        #If position is out of bounds
        if curr_node is None:
            print("Position is out of bounds")
            return

        #Delete node
        previous_node.next = curr_node.next
        curr_node = None
        



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#llist.prepend("E")

#llist.inset_after_node(llist.head.next, "E")
#llist.delete_node("B")
llist.del_node_pos(3)



llist.print_list()
