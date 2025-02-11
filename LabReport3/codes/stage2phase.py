import numpy as np
import matplotlib.pyplot as plt

# Define component values
R = 1e3  # 1 kOhm
C = 100e-9  # 100 nF

# Define frequency range
s = np.logspace(1, 4, 1000) 
w=2*np.pi*s
tan_inv = np.arctan(-2*R*w*C/(1-(R*w*C)**2)) * (180 / np.pi)  # Convert to degrees
#tan_inv =2*np.arctan(-R * C * w) * (180 / np.pi) 
plt.figure(figsize=(8, 6))
x = [100, 1000, 10000]
y=[-14.4 ,  -60.48, 48.24]
plt.scatter(x, y, color='red', label="Readings")
for x, y in zip(x, y):
    plt.annotate(f"({x}, {y})", (x, y), textcoords="offset points", xytext=(5,5), ha='right', fontsize=10, color='black')

plt.semilogx(s, tan_inv, color='blue')
plt.xlabel("log(s) ")
plt.ylabel("Phase Diff (degrees)")
plt.title("Phase Bode plot Stage 2")
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig("../figs/Stage2/Phase.png")
plt.show()

