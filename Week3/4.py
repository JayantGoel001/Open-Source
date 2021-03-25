import numpy as np

z = np.ones((3, 3))
z = np.pad(z, pad_width=1, mode='constant', constant_values=0)
print(z)
