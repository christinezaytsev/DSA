# Find parition index then recursively sort left and right parts.
# Stop recursion when there is one element left (start >= end).
def quicksort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)
        quicksort(arr, start, partition_index-1)
        quicksort(arr, partition_index+1, end)

# Select pivot element and rearrange list so that elements 
# to left are less and elements to right are greater than pivot. 
# The final position of the pivot is the partition index.
def partition(arr, start, end):
    pivot = end
    partition_index = start
    for i in range(start, end):
        if arr[i] <= arr[pivot]:
            arr = swap(arr, i, partition_index)
            partition_index += 1
    swap(arr, partition_index, pivot)
    return partition_index

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr


if __name__ == '__main__':
    arr = [4, 2, 0, 3, -1, 5, -2]
    print('unsorted array:    ', arr)
    quicksort(arr, 0, len(arr)-1)
    print('quicksorted array: ', arr)

