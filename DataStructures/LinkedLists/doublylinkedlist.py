class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        curr_node = self.head
        if not curr_node:
            self.head = new_node
        else:
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
        
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

if __name__ == '__main__':
    double_list = DoublyLinkedList()
    double_list.append('mars')
    double_list.append('juin')
    double_list.append('juillet')
    double_list.print_list()