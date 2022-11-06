import numpy as np
import matplotlib.pyplot as plt

path50 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Lab-5-Different-Averaging-Widths/num50.csv"
data50 = np.genfromtxt(path50, delimiter=',', names =True,invalid_raise = False)
time50 = data50['Time']-953
strength50 = data50['Value']

fig, ax = plt.subplots()

ax.plot(time50,strength50, color='darkgreen')
ax.set_xlim(0,3000)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Strength (Au)')
ax.set_title('Signal Smoothing')

plt.show()
