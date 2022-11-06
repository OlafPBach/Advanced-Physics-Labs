import numpy as np
import matplotlib.pyplot as plt

path1 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Lab-5-Different-Averaging-Widths/num1.csv"
data1 = np.genfromtxt(path1, delimiter=',', names =True,invalid_raise = False)
time1 = data1['Time']-953
strength1 = data1['Value']

path5 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Lab-5-Different-Averaging-Widths/num5.csv"
data5 = np.genfromtxt(path5, delimiter=',', names =True,invalid_raise = False)
time5 = data5['Time']-2000
strength5 = data5['Value']

path10 = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Lab-5-Different-Averaging-Widths/num10.csv"
data10 = np.genfromtxt(path10, delimiter=',', names =True,invalid_raise = False)
time10 = data10['Time']-4150
strength10 = data10['Value']

fig, ax = plt.subplots()

ax.plot(time1,strength1, color='lightsteelblue')
ax.plot(time5,strength5, color='lightcoral')
ax.plot(time10,strength10, color='black')
ax.set_xlim(0,2000)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Strength (Au)')
ax.set_title('Signal Smoothing')

plt.show()
