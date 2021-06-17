import numpy as np
import matplotlib.pyplot as plt

n = 256

X = np.linspace(-np.pi, np.pi, n, endpoint=True)
y = np.sin(2 * X)

plt.plot(X, y + 1, color="blue", alpha=1.00)
plt.plot(X, y - 1, color="green", alpha=1.00)
plt.show()