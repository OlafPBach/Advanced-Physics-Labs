import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

x=[]
y=[]

with open('labdata.csv','r') as File:
    Line_reader = csv.reader(File)
    for row in Line_reader:
        x.append(row[0])
        y.append(float(row[1]))

fig, ax=plt.subplots()
ax.tick_params(labelsize=8)
ax.plot(x,y,color='g')
plt.ylim(20,35)
plt.xticks(np.arange(0,150,10))
plt.xlabel('Time (10s)')
plt.ylabel('Temperature (C)')
ax.set_title('Temperature over Time')