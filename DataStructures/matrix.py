sample_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
zero_matrix = [ [ 0 for _ in range(len(sample_matrix[0])) ] for _ in range(len(sample_matrix)) ]

# Select all columns using [:]
copied_matrix = [row[:] for row in sample_matrix]

# zip() inverts into a list of tuples. We need to convert back into list of lists.
transposed_matrix = [list(i) for i in zip(*sample_matrix)]


print('sample_matrix: ', sample_matrix)
print('zero_matrix: ', zero_matrix)
print('copied_matrix: ', copied_matrix)
print('transposed_matrix: ', transposed_matrix)

# Samples of how to indexing 2D array:
print('second row of sample_matrix: ', sample_matrix[1])
print('second column of sample_matrix: ', [row[1] for row in sample_matrix])
print('second third of sample_matrix: ', sample_matrix[:][2])
print('second element in second column of sample_matrix: ', sample_matrix[1][1])

