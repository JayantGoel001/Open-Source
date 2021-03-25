import numpy as np
n = int(input())
m = int(input())

matrix = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        matrix[i][j] = int(input())

print(np.linalg.matrix_rank(matrix))
print(np.trace(matrix))
print(np.linalg.det(matrix))