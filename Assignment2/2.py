import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 400)


y1 = 2 * x + 1
y2 = 2 * x + 2
y3 = 2 * x + 3


plt.figure(figsize=(10, 10))


plt.plot(x, y1, color='blue', linestyle='-', label='y = 2x + 1')
plt.plot(x, y2, color='red', linestyle='--', label='y = 2x + 2')
plt.plot(x, y3, color='green', linestyle='-.', label='y = 2x + 3')


plt.title('Graphs of y = 2x + 1, y = 2x + 2, and y = 2x + 3', fontsize=10)
plt.xlabel('x-axis', fontsize=10)
plt.ylabel('y-axis', fontsize=10)


plt.grid(True, linestyle=':', color='gray')


plt.legend()


plt.show()
