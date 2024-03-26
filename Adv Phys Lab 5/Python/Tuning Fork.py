import numpy as np
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Lab-2/main/Lab1-Oscillascope-Data"
data = np.genfromtxt(path, delimiter=',', names =True,invalid_raise = False)
freq = data['Frequency']
strength = data['Amplitudes']+108

fig, ax = plt.subplots()

from scipy.signal import find_peaks
peaks, _ = find_peaks(strength, height=65)
print('First peak is at: '+str(peaks[0]) )
print('which corresponds to a frequency of '+str( freq[peaks[0]] )+' Hertz')

ax.plot(freq,strength, color='gray')
ax.plot(892.71559,75 ,"x",color='red')
ax.set_xlim(0,2000)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude')
ax.set_title('Tuning Fork')

plt.show()