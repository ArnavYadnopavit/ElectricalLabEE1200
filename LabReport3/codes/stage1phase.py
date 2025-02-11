import numpy as np
import matplotlib.pyplot as plt
#array([  0.  ,  25.92,  77.76,  14.4 ,  60.48, 138.24,  14.4 ,  86.4 ,169.2 ])

# Define component values
R = 1e3  # 1 kOhm
C = 100e-9  # 100 nF

# Define frequency range
s = np.logspace(1, 6, 1000) 
w=2*np.pi*s
tan_inv = np.arctan(-R * C * w) * (180 / np.pi)  # Convert to degrees
plt.figure(figsize=(8, 6))
x = [100, 1000, 10000]
y=[0.  ,  -25.92,  -77.76]
plt.scatter(x, y, color='red', label="Readings")
for x, y in zip(x, y):
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(5,5), ha='right', fontsize=10, color='black')

plt.semilogx(s, tan_inv, color='blue')
plt.xlabel("log(s) ")
plt.ylabel("Phase Diff (degrees)")
plt.title("Phase Bode plot Stage1")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig("../figs/Stage1/Phase.png")
plt.show()

