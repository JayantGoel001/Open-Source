# 1
import numpy as np

# 2
z = np.arange(10, 50)
print(z)

# 3
print(z[::-1])

# 4
z = np.arange(9).reshape((3, 3))
print(z)

# 5
l = [1, 2, 0, 0, 4, 0]
print(np.nonzero(l))

# 6
z = np.eye(3)
print(z)

# 7
z = np.random.random((3, 3, 3))
print(z)

# 8
z = np.random.random((10, 10))
print(z.min(), z.max())

# 9
z = np.random.random(30)
print(z.mean())

# 10
z = np.ones((10, 10))
z[1:-1, 1:-1] = 0
print(z)

# 11
z = np.ones((5, 5))
z = np.pad(z, pad_width=1, mode='constant', constant_values=0)
print(z)

# 12
z1 = np.random.random((5, 3))
z2 = np.random.random((3, 2))
print(np.dot(z1, z2))

# 13
z = np.arange(0, 20)
z[(3 < z) & (z < 8)] *= -1
print(z)

# 14
z1 = np.random.randint(0, 20, 10)
z2 = np.random.randint(0, 20, 10)
print(np.intersect1d(z1, z2))

# 15
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(yesterday)
print(today)
print(tomorrow)

# 16
z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(z)

# 17
z1 = np.random.randint(0, 2, 5)
z2 = np.random.randint(0, 2, 5)
print(np.allclose(z1, z2))
print(np.array_equal(z1, z2))

# 18
z = np.random.random(10)
z[z.argmax()] = 0
print(z)