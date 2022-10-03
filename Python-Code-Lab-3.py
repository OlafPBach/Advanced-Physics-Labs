import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/lab3data.csv"
data = np.genfromtxt(path, delimiter=',', names =True,invalid_raise = False)
time = data['Time']/10
sensorValue = data['RawPot']/100 + 22
RawTemp = data['RawTemp']

A = 0.003354016
B = 0.0002993410
C = 0.000002135133
D = -0.000000005672000

V2 = ((RawTemp)/204.6)
 
R2 = (V2*3.3)/(5-V2)
 
St = np.log(R2/3.3)
TR = (A + B*St + C*St**2 + D*St**3)**(-1) - 273.5

fig, ax = plt.subplots()

ax.plot(time,TR, color='red')
ax.plot(time,sensorValue, color='green')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature (C)')
ax.set_title('Temp Change')

plt.show()