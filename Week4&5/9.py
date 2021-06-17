from scipy import cluster, constants, fftpack, integrate, interpolate, io, linalg, ndimage, odr, optimize, signal, \
    sparse, spatial, special
import numpy as np

# 1
ar = np.ones((4, 4))
np.savetxt("test.text", ar)

# 2
x = [27, 64, 891]
print(special.cbrt(x))

# 3

ar1 = np.zeros((2, 2))
ar2 = np.zeros((2, 2))

ar1 = [[4, 5], [3, 2]]
ar2 = [[4, 5], [3, 2]]

print(linalg.det(ar1))

# 4
print(linalg.inv(ar1))

# 5
ar2 = [[5, 4], [6, 3]]
print(linalg.eigvals(ar2))
print(linalg.eig(ar2)[1])

# 6
m = [[1, 2, 0], [0, 0, 3], [4, 0, 5]]
A = sparse.csr_matrix(m)
c = [1, 0, -1]
v = sparse.csr_matrix(c)
print(A.multiply(v).todense())
