import numpy as np
import matplotlib.pyplot as plt

# Define component values
R = 1e3  # 1 kOhm
C = 1e-7  # 100 nF
#array([  0,-0.81643989,-28.54232711,0.,-8.31030888, -57.64807176,0.,-17.35001135,-59.13023121])

# Define frequency range
s = np.logspace(1, 6, 1000)  # from 10^1 to 10^6 rad/s
w=2*np.pi*s
Hs = 1 / (1 + R * C * w)  # Compute H(s)

# Convert to dB scale
magnitude_dB = 20 * np.log10(np.abs(Hs))

# Plot the magnitude response
plt.figure(figsize=(8, 6))
plt.semilogx(s, magnitude_dB, label="Bode Magnitude")

# Plot given points
points_x = [100, 1000, 10000]
points_y = [0,-0.81643989,-28.54232711]
plt.scatter(points_x, points_y, color='red', label="Readings")

# Annotate points
for x, y in zip(points_x, points_y):
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(5,5), ha='right', fontsize=10, color='black')

plt.xlabel("log(s) (rad/s)")
plt.ylabel("20log|H(s)| (dB)")
plt.title("Bode Magnitude Plot")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig("../figs/Stage1/Magn.png")
plt.show()

