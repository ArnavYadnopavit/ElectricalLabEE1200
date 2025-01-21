import numpy as np
import matplotlib.pyplot as plt

V1 = np.linspace(-(2)**0.5, 2**0.5, 1000000)
V2 = np.sqrt(2)*V1*np.sqrt(2-V1**2)*(1-V1**2)
V_2=-np.sqrt(2)*V1*np.sqrt(2-V1**2)*(1-V1**2)

# Create the plot
plt.figure(figsize=(8, 8))
plt.plot(V1, V2, label='$V_1$ vs $V_2$', color='blue')
plt.plot(V1, V_2, color='blue')
# Label the axes
plt.xlabel('$V_1$ (V)', fontsize=12)
plt.ylabel('$V_2$ (V)', fontsize=12)

# Add a title and legend
plt.title('Phase-Space Plot of $V_1$ vs $V_2$', fontsize=14)
plt.legend()

# Show the grid
plt.grid(True)

# Display the plot
plt.savefig("../figs/6/pyplot.png")
