class MinHeap:
    def __init__(self, arr):
        self.items = arr

    def getLeftChildIndex(self, parent_index):
        return 2 * parent_index + 1
    
    def getRightChildIndex(self, parent_index):
        return 2 * parent_index + 2
    
    def getParentIndex(self, child_index):
        return (child_index - 1) // 2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.items)
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self.items)
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def swap(self, index1, index2):
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp
    
    # Return root (the minimum value in min-heap)
    def peek(self):
        if len(self.items) == 0:
            raise ValueError('Heap is empty') 
        return self.items[0]
    
    # Remove root from min-heap, replace it with last element, shrink array by 1, and bubble down to correct location
    def poll(self):
        if len(self.items) == 0:
            raise ValueError('Heap is empty') 
        self.items[0] = self.items[-1]
        self.items = self.items[:-1]
        self.heapifyDown()
        return self.items
    
    # Add new item to end, then bubble item up heap to correct location
    def add(self, item):
        self.items.append(item)
        self.heapifyUp()
        return self.items
    
    def heapifyUp(self):
        curr_index = len(self.items) - 1
        # while the value of parent is greater than value of curr_index, bubble up by swapping with parent index
        while self.hasParent(curr_index) and self.items[self.getParentIndex(curr_index)] > self.items[curr_index]:
            self.swap(self.getParentIndex(curr_index), curr_index)
            curr_index = self.getParentIndex(curr_index)

    def heapifyDown(self):
        curr_index = 0
        # if there is no left child, there definitely is no right child (heap fills left to right)
        while(self.hasLeftChild(curr_index)):
            # we need to determine which child (left or right) is smaller
            smaller_child_index = self.getLeftChildIndex(curr_index)
            if self.hasRightChild(curr_index) and self.items[self.getLeftChildIndex(curr_index)] > self.items[self.getRightChildIndex(curr_index)]:
                smaller_child_index = self.getRightChildIndex(curr_index)
            if self.items[curr_index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(curr_index, smaller_child_index)
            curr_index = smaller_child_index

if __name__ == '__main__':
    heap = MinHeap([0, 1, 3, 5, 4])
    print('poll: ', heap.poll())
    print('add: ', heap.add(2))

        


    



