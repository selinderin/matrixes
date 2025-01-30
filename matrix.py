import numpy as np

# task1
elements = np.array([10, 20, 30, 40])
minimum = np.min(elements)
print(minimum)

# task2
elements = np.array([10, 20, 30, 40])
sum_of_elements = np.sum(elements)
print(sum_of_elements)

# task3
def countFreq(arr, target):
    res = 0
    for i in range(len(arr)):
        if arr[i] == target:
            res += 1
    return res

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
print(countFreq(arr, target))

# task4
def find_indices(matrix, target):
    indices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                indices.append((i, j))
    return indices

matrix = [[1, 2, 3], [4, 2, 6], [7, 8, 2]]
target = 2
print(find_indices(matrix, target))

# task 5
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_main_diag = np.trace(matrix)
print(sum_main_diag)

# Task 6
sum_secondary_diag = np.trace(np.fliplr(matrix))
print(sum_secondary_diag)

# Task 7
max_in_columns = np.max(matrix, axis=0)
print(max_in_columns)

# Task 8
row_with_max_sum = np.argmax(np.sum(matrix, axis=1))
print(row_with_max_sum)

# Task 9
column_with_min_sum = np.argmin(np.sum(matrix, axis=0))
print(column_with_min_sum)

# Task 10
unique_elements = np.unique(matrix)
print(unique_elements)