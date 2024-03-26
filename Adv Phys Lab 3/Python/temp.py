import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

path = "https://raw.githubusercontent.com/OlafPBach/Advanced-Physics-Labs/main/test-data-for-lab-4.csv"
data = np.genfromtxt(path, delimiter=',', names=True)

print(data)