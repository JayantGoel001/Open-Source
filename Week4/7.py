import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

x = [-pi, -pi/4, -pi/2, 0, pi/4, pi/2, pi]
try:
    y1 = np.tan(x)
    y2 = 1/y1
    y3 = 1/np.cos(x)
    y4 = 1/np.sin(x)

    plt.plot(x, y1, color="red", label='tan')
    plt.plot(x, y2, color="green", label='Cot')
    plt.plot(x, y3, color="blue", label='Sec')
    plt.plot(x, y4, color="yellow", label='Cosec')
    plt.legend()

    plt.show()
except:
    print("Error")