import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = e^(-4 * sin(2 * pi * x))
def f(x):
    return np.exp(-4 * np.sin(2 * np.pi * x))

# Generate 1000 evenly spaced x values from 0 to 1
x_values = np.linspace(0, 1, 1000)

# Compute the function values
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, label=r'$f(x) = e^{-4 \sin(2\pi x)}$')
plt.title('Plot of f(x) = e^{-4 sin(2πx)}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
