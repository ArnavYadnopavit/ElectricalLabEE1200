import numpy as np
import matplotlib.pyplot as plt

# Define component values
R1 = R2 = 1000  # Ohms
C1 = C2 = 1e-6  # Farads

# Define frequency range
frequencies = np.logspace(1, 5, 500)  # 10 Hz to 100 kHz
omega = 2 * np.pi * frequencies  # Convert to angular frequency
# Compute transfer function for Low-Pass Filter
wc = 1 / np.sqrt(R1 * R2 * C1 * C2)  # Cutoff frequency
s = 1j * omega
H_s_lpf = (wc**2) / (s**2 + (wc / 0.5) * s + wc**2)

# Magnitude and phase
magnitude_lpf = 20 * np.log10(np.abs(H_s_lpf))
phase_lpf = np.angle(H_s_lpf, deg=True)

# Plot Bode magnitude response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude_lpf)
plt.title("Bode Plot of Low-Pass Filter")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid(which="both", linestyle="--")

# Plot Bode phase response
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase_lpf)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.grid(which="both", linestyle="--")

plt.show()

