import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.title("Cosine Graph")
plt.show()

plt.plot(X, S)
plt.title("Sine Graph")
plt.show()