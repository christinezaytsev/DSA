"""
Python deque is recommended way to create stack/queue.
It's implemented using doubly-linked lists.
Better for memory allocation: don't need to copy elements,
unlike a list, which is implemented using dynamic array.
"""
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    boulangerie_stack = Stack()
    boulangerie_stack.push('une baguette')
    boulangerie_stack.push('un croissant')
    boulangerie_stack.push('un pain')
    boulangerie_stack.push('une tarte')
    
    print(boulangerie_stack.peek())
    print(boulangerie_stack.size())
    boulangerie_stack.pop()
    print(boulangerie_stack.stack)
