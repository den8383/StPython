import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [5,6,7,8]
plt.plot(x,y, 'o-', label = "my data")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc = 'best')
plt.show()
