import numpy as np
import matplotlib.pyplot as plt

path1 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Lab-6-Data.csv"
data1 = np.genfromtxt(path1, delimiter=',', names =True,invalid_raise = False)
time1 = data1['Time']-1500
strength1 = data1['Value']

path5 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Lab-6-Data-Capacitor.csv"
data5 = np.genfromtxt(path5, delimiter=',', names =True,invalid_raise = False)
time5 = data5['Time']-1500
strength5 = data5['Value']

fig, ax = plt.subplots()

ax.plot(time1,strength1, color='lightsteelblue')
ax.plot(time5,strength5, color='lightcoral')
ax.set_xlim(0,2000)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Strength (Au)')
ax.set_title('Electronic Audio Filter')

plt.show()
