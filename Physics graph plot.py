#importing modules
import numpy as np
from matplotlib import pyplot as plt
#setting plot style
plt.style.use(['default'])
#making array of plot points
x=[62.002,71.99,85.01,99.99,111.99,120.005,133.99,148.01]
y=[1.58**2,1.705**2,1.849**2,2.009**2,2.119**2,2.201**2,2.319**2,2.449**2]
#sizing the plot
plt.figure(figsize=(8,4))
#modifying plot 
plt.plot(x,y,'.--',lw=0.8,color='red')
#Axis number size
plt.tick_params(axis='both',labelsize=10)
#Axis Labels
plt.xlabel('L[cm]')
plt.ylabel('$T^2[s^2]$')
#adding grid
plt.grid()
#giving title
plt.title('Pendelum\n$T^2$ vs $l$')
#Saving the graph
plt.savefig('fig',  format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None, 
       )
#showing the plot
plt.show()


