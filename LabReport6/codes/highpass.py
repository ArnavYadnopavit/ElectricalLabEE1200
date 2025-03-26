import numpy as np
import matplotlib.pyplot as plt

# Define component values
R1 = R2 = 1000  # Ohms
C1 = C2 = 1e-6  # Farads

# Define frequency range
frequencies = np.logspace(1, 5, 500)  # 10 Hz to 100 kHz
omega = 2 * np.pi * frequencies  # Convert to angular frequency

# Compute transfer function manually
wc = 1 / np.sqrt(R1 * R2 * C1 * C2)  # Cutoff frequency
s = 1j * omega
H_s = (s**2) / (s**2 + (wc / 0.5) * s + wc**2)  # HPF transfer function

# Magnitude and phase
magnitude = 20 * np.log10(np.abs(H_s))
phase = np.angle(H_s, deg=True)

# Experimental data points
exp_frequencies = np.array([100, 160, 200, 1000])
exp_gains = np.array([-10.46, -7.12, -5.04, -0.238])

# Plot Bode magnitude response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude, label="Theoretical Response")
plt.scatter(exp_frequencies, exp_gains, color='red', label="Experimental Data", zorder=3)
plt.title("Bode Plot of High-Pass Filter")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.grid(which="both", linestyle="--")

# Plot Bode phase response
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase, label="Theoretical Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.legend()
plt.grid(which="both", linestyle="--")
plt.show()
