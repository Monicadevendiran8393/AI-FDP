import numpy as np
import matplotlib.pyplot as plt
txt1 = "The plot between the width changes Vs different standard deviations"
txt2 = "The plot between height and the position of peak and Vs different means"
def normal(x, mean, sd):
    y = 1 / (sd * np.sqrt(2 * np.pi)) * np.exp(-((x - mean) ** 2) / (2 * sd**2))
    return y
mean = 1
sd1, sd2, sd3 = 10, 3, 4
X1 = np.arange(mean - 5 * sd1, mean + 5 * sd1, 0.01)
X2 = np.arange(mean - 5 * sd2, mean + 5 * sd2, 0.01)
X3 = np.arange(mean - 5 * sd3, mean + 5 * sd3, 0.01)
Y1 = normal(X1, mean, sd1)
Y2 = normal(X2, mean, sd2)
Y3 = normal(X3, mean, sd3)
plt.figure(figsize=(12, 6))
plt.plot(X1, Y1, label=f"mean{mean} Standard deviation {sd1}")
plt.plot(X2, Y2, label=f"mean{mean} Standard deviation {sd2}")
plt.plot(X3, Y3, label=f"mean{mean} Standard deviation {sd3}")
plt.legend()
plt.title("Gaussian distributions")
plt.xlabel("X")
plt.ylabel("Y")
plt.figtext(0.5,0.01,txt1,wrap=True,horizontalalignment="center",fontsize=8,bbox={"facecolor": "blue", "alpha": 0.3, "pad": 3},)
plt.grid(True)
plt.show()

sd = 2
mean1, mean2, mean3 = 10, 2, 4
X1 = np.arange(mean1 - 5 * sd, mean1 + 5 * sd, 0.1)
X2 = np.arange(mean2 - 3 * sd, mean2 + 3 * sd, 0.1)
X3 = np.arange(mean3 - 3 * sd, mean3 + 3 * sd, 0.1)
Y1 = normal(X1, mean1, sd)
Y2 = normal(X2, mean2, sd)
Y3 = normal(X3, mean3, sd)
plt.figure(figsize=(12, 6))
plt.plot(X1, Y1, label=f"mean {mean1} Standard deviation {sd}")
plt.plot(X2, Y2, label=f"mean {mean2} Standard deviation {sd}")
plt.plot(X3, Y3, label=f"mean {mean3} Standard deviation {sd}")
plt.legend()
plt.title("Gaussian distributions")
plt.xlabel("X")
plt.ylabel("Y")
plt.figtext(0.5,0.01,txt2,wrap=True,horizontalalignment="center",fontsize=8,bbox={"facecolor": "blue", "alpha": 0.3, "pad": 5},)
plt.grid(True)
plt.show()
