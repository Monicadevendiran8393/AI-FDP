import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_interp):
    """
    Perform Lagrange interpolation.

    Parameters:
    x (array_like): Array of x-coordinates of data points.
    y (array_like): Array of y-coordinates of data points.
    x_interp (float): The x-coordinate where interpolation is desired.

    Returns:
    float: The interpolated y-coordinate at x_interp.
    """
    n = len(x)
    result = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_interp - x[j]) / (x[i] - x[j])
        result=result+term

    return result

def polynomial(x):
    return 2*x**4 - 3*x**3 + 7*x**2 - 23*x + 8

x_values = np.arange(-5, 5.1, 0.1)
y_values = polynomial(x_values)

x_interp = np.arange(-5, 5.1, 0.1)
y_interp = [lagrange_interpolation(x_values, y_values, xi) for xi in x_interp]

plt.plot(x_values, y_values, label='Original Polynomial')
plt.plot(x_interp, y_interp, label='Lagrange Interpolation', linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Interpolation of y = 2x^4 - 3x^3 + 7x^2 - 23x + 8')
plt.legend()
plt.grid(True)
plt.show()
