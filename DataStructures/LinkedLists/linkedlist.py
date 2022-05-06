class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList: 
    def __init__(self):
        self.head = None
    
    def print_list(self):
        curr_node = self.head
    
        # continue until there is no next node
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
    
    def append(self, data):
        new_node = Node(data)
    
        # head pointer doesn't point to anything; there aren't any nodes yet
        if self.head is None:
            self.head = new_node
            return
    
        curr_node = self.head
        # move head pointer right until there are no more nodes
        while curr_node.next:
            curr_node = curr_node.next
        # append new node
        curr_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
    
        # head pointer doesn't point to anything; there aren't any nodes yet
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after_node(self, prev_node: Node, data):
        new_node = Node(data)
    
        new_node.next = prev_node.next
        prev_node.next = new_node
    

    def delete(self, key):
        curr_node = self.head
        if curr_node and key == curr_node:
            self.head = curr_node.next
            curr_node = None
    
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
    
        if not curr_node:
            return
    
        prev.next = curr_node.next
        curr_node = None

    def reverse_iterative(self):
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    
    
    def reverse_recursive(self):

        def recursive_helper(curr: Node, prev: Node):
            # this replicates check in 'while curr:' loop above
            if not curr:
                return prev
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            # remember to RETURN recursive function call!
            return recursive_helper(curr, prev)

        # eventually self.head = prev when reaching base case    
        self.head = recursive_helper(curr=self.head, prev=None)
    

    def find_midpoint(self):
        """
        Returns the midpoint of linked list.
        If there are two middle nodes, return the second middle node.
        Use slow & fast pointer to solve, where fast moves 2 steps for every 1 slow step.
        """
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
            

 
if __name__ == '__main__':
   linklist = LinkedList()
   linklist.append("B")
   linklist.append("D")
   linklist.prepend("A")
   linklist.insert_after_node(linklist.head.next, "C")
   linklist.delete("D")
   linklist.print_list()

   print('reverse recursively:')
   linklist.reverse_recursive()
   linklist.print_list()

   
   print('reverse iteratively:')
   linklist.reverse_iterative()
   linklist.print_list()

   print('midpoint:')
   print(linklist.find_midpoint().data)


