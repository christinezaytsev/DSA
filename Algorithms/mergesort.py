def merge_sort(arr):
    # Recursively split array in half until 1 element remains, then merge
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge step
        # Keep track of index in left, right, and merged arrays
        left_index = 0
        right_index = 0
        merge_index = 0

        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                arr[merge_index] = left_arr[left_index]
                left_index += 1
            else:
                arr[merge_index] = right_arr[right_index]
                right_index += 1
            merge_index += 1
        
        # Consider that one array is longer, so merge remaining elements without comparing
        while left_index < len(left_arr):
            arr[merge_index] = left_arr[left_index]
            left_index +=1
            merge_index +=1 
        while right_index < len(right_arr):
            arr[merge_index] = right_arr[right_index]
            right_index +=1
            merge_index +=1 


if __name__ == '__main__':
    test_arr = [-1, 3, 0, 2, 4, -6]
    merge_sort(test_arr)
    print(test_arr)