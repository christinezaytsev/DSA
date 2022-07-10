from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        self.queue.popleft()

if __name__ == '__main__':
    couleurs = Queue()
    couleurs.enqueue('rouge')
    couleurs.enqueue('orange')
    couleurs.enqueue('jaune')
    couleurs.dequeue()
    print(couleurs.queue)
