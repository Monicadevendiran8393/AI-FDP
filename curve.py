import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean_values = [0, 2, 4]  # Different means
variance_constant = 1  # Constant variance

# Plot different means (constant variance)
plt.figure(figsize=(10, 6))
for i, mean in enumerate(mean_values):
    x = np.linspace(mean - 3 * np.sqrt(variance_constant), mean + 3 * np.sqrt(variance_constant), 1000)
    y = norm.pdf(x, mean, np.sqrt(variance_constant))
    plt.plot(x, y, label=f"Mean = {mean}", color=['violet', 'blue', 'brown'][i])

plt.title("Normal Distribution with Different Means (Constant Variance)")
plt.xlabel("X-axis")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

# Parameters for different variances (constant mean)
variance_values = [0.5, 1, 2]  # Different variances
mean_constant = 2  # Constant mean

# Plot different variances (constant mean)
plt.figure(figsize=(10, 6))
for i, variance in enumerate(variance_values):
    x = np.linspace(mean_constant - 3 * np.sqrt(variance), mean_constant + 3 * np.sqrt(variance), 1000)
    y = norm.pdf(x, mean_constant, np.sqrt(variance))
    plt.plot(x, y, label=f"Variance = {variance}", color=['violet', 'blue', 'brown'][i])

plt.title("Normal Distribution with Different Variances (Constant Mean)")
plt.xlabel("X-axis")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
