import numpy as np
import matplotlib.pyplot as plt

n = 12

X = np.arange(n)
y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, y1, facecolor="#9999ff", edgecolor='white')
plt.show()

y2 = (1 - X/float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, y2, facecolor="#ff9999", edgecolor='white')
plt.show()