import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,100,10000)
y1 = np.arctan(0.01*x) - np.arctan(0.1*x)
y2 = np.arctan(10*x) - np.arctan(x)
plt.plot(x,y1)
plt.show()
plt.plot(x,y2)
plt.show()
