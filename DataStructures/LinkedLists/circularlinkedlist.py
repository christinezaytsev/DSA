"""
In circular linked lists, next of the last node
points to the head node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        # if the linked list is empty, set head to new node and point to itself
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head
    
    def print_list(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.data)
            if curr_node.next == self.head:
                break
            curr_node = curr_node.next

if __name__ == '__main__':
    circ_list = CircularLinkedList()
    circ_list.append('lundi')
    circ_list.append('mardi')
    circ_list.print_list()
        

        
