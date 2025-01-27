import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])


plt.figure(figsize=(8, 6))
plt.scatter(x, y, marker='*', color='green', label='Data points')


plt.title('Scatter Pattern of Points (x, y)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)


plt.grid(True, linestyle=':', color='gray')


plt.legend()


plt.show()
