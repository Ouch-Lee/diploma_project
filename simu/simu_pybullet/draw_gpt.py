import numpy as np
import matplotlib.pyplot as plt

def gaussian_distribution(x, mean, std_dev):
    """Calculate the Gaussian distribution"""
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))

# Generate data points
x = np.linspace(90, 130, 100)
mean = 110  # Mean of the Gaussian distribution
std_dev = 4.745  # Standard deviation of the Gaussian distribution

# Calculate the Gaussian distribution for the given data points
y = gaussian_distribution(x, mean, std_dev)

# Plot the Gaussian distribution
plt.plot(x, y)
plt.title('D-PDF')
plt.xlabel('D')
plt.ylabel('P')
plt.grid(True)
plt.show()