import numpy as np
import matplotlib.pyplot as plt

n = 1024

X = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
plt.scatter(X, y)
plt.show()