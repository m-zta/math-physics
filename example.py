import numpy as np
import matplotlib.pyplot as plt

# Define bounds and step size
a = -1
b = 1
step = 0.25


# Define x and y
num = int((b - a) / step + 1)
x = np.linspace(a, b, num)
y = 2 * x ** 2 + 1

# Scatter plot with lines between points
plt.scatter(x, y, color='gray')
plt.plot(x, y, color='black')

# Make the plot look nice
plt.xlim((- (1 + step), 1 + step))
plt.ylim((-1, 5))
plt.xticks((-1, 0, 1))
plt.yticks(np.arange(0, 5, 2))
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = 2x^2 + 1')
plt.grid(True)

# Show the plot
plt.show()
