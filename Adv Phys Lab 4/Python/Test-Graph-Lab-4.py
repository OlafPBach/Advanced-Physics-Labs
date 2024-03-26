import numpy as np
import matplotlib.pyplot as plt


path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/Test-Signal-Lab-4.csv"
data = np.genfromtxt(path, delimiter=',', names=True)
data.dtype.names

Time = (data['Time'])
Strength = data['Luminence']

fig, ax = plt.subplots()
ax.plot(Time,Strength)
plt.xlim(0,20000)
plt.show()

from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq

Millis = np.linspace(1,len(Time),len(Time))

SAMPLE_RATE = 1000 #millisecond/second
DURATION = 20 #seconds

N = len(Time)

yf = fft(Strength)
xf = fftfreq(N, 1/SAMPLE_RATE)
from scipy.signal import find_peaks
peaks, _ = find_peaks(np.abs(yf), height=10000)
print('First peak is at: '+str(peaks[0]) )
print('which corresponds to a frequency of '+str( xf[peaks[0]] )+' Hertz')

fig, ax = plt.subplots()
ax.plot(xf, np.abs(yf),color='blue')
ax.plot(xf[peaks[0]],np.abs(yf[peaks[0]]) ,"x",color='red')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('')
ax.set_title('Signal')
ax.set_xlim(0,4)
ax.set_ylim(0,3e6)
ax.grid()
plt.show()

