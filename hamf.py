#for python3
#sudo apt install python3-pip
#pip3 install numpy
#pip3 install matplotlib

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.5, 500)
s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)
plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.plot(t, s)
plt.show()
