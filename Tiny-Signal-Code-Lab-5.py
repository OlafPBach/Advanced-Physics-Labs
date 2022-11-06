import numpy as np
import matplotlib.pyplot as plt

path1 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Tiny-Signal-Date-Lab-5"
data1 = np.genfromtxt(path1, delimiter=',', names =True,invalid_raise = False)
time1 = data1['Time']-4143
strength1 = data1['Value']

fig, ax = plt.subplots()

ax.plot(time1,strength1, color='black')
ax.set_xlim(0,6504-4143)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Strength (Au)')
ax.set_title('Tiny Signal')

plt.show()
