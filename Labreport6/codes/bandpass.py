import numpy as np
import matplotlib.pyplot as plt

# Define component values for High-Pass Filter (HPF)
R1_HPF = R2_HPF = 1000  # Ohms
C1_HPF = C2_HPF = 1e-6  # Farads

# Define component values for Low-Pass Filter (LPF)
R1_LPF = R2_LPF = 100  # Ohms
C1_LPF = C2_LPF = 1e-6  # Farads

# Define frequency range
frequencies = np.logspace(1, 5, 500)  # 10 Hz to 100 kHz
omega = 2 * np.pi * frequencies  # Convert to angular frequency

# Compute cutoff frequencies
wc1 = 1 / np.sqrt(R1_HPF * R2_HPF * C1_HPF * C2_HPF)  # High-Pass cutoff
wc2 = 1 / np.sqrt(R1_LPF * R2_LPF * C1_LPF * C2_LPF)  # Low-Pass cutoff

# Define the complex frequency variable s
s = 1j * omega

# Transfer Function of High-Pass Filter (HPF)
H_HPF = (s**2) / (s**2 + (wc1 / 0.5) * s + wc1**2)

# Transfer Function of Low-Pass Filter (LPF)
H_LPF = (wc2**2) / (s**2 + (wc2 / 0.5) * s + wc2**2)

# Transfer Function of Bandpass Filter (BPF)
H_BPF = H_HPF * H_LPF

# Compute Magnitude (in dB) and Phase (in degrees)
magnitude_HPF = 20 * np.log10(np.abs(H_HPF))
phase_HPF = np.angle(H_HPF, deg=True)

magnitude_LPF = 20 * np.log10(np.abs(H_LPF))
phase_LPF = np.angle(H_LPF, deg=True)

magnitude_BPF = 20 * np.log10(np.abs(H_BPF))
phase_BPF = np.angle(H_BPF, deg=True)

# Plot Bode Magnitude Response
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude_HPF, label="HPF Magnitude")
plt.semilogx(frequencies, magnitude_LPF, label="LPF Magnitude")
plt.semilogx(frequencies, magnitude_BPF, label="BPF Magnitude", linestyle='dashed')
plt.title("Bode Plot of Bandpass Filter")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.grid(which="both", linestyle="--")

# Plot Bode Phase Response
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase_HPF, label="HPF Phase")
plt.semilogx(frequencies, phase_LPF, label="LPF Phase")
plt.semilogx(frequencies, phase_BPF, label="BPF Phase", linestyle='dashed')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (degrees)")
plt.legend()
plt.grid(which="both", linestyle="--")

plt.tight_layout()
plt.show()

